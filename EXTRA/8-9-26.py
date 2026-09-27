"""
=================================================================
 CANTEEN AI FOOD RECOMMENDER CHATBOT  (NLTK version)
=================================================================
Combines:
  - NLTK for natural-language understanding (tokenizing,
    lemmatizing, intent matching)
  - Item-based collaborative filtering (cosine similarity) for
    the actual food recommendations

FIRST-TIME SETUP
-----------------
Install requirements:
    pip install pandas scikit-learn nltk

Then download the NLTK data (only needed once — the script also
does this automatically on first run):
    python -m nltk.downloader punkt punkt_tab wordnet omw-1.4

HOW TO USE
----------
1. Update the CONFIG section below with your actual CSV file
   names and column names.
2. Run:  python canteen_ai_chatbot_nltk.py
3. Enter your Student ID, then chat with the bot
   (try: "recommend something", "I'm hungry", "what's good today").
=================================================================
"""

import sys
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# ============================================================
# 0. CONFIG  (edit these to match your actual files/columns)
# ============================================================

CONFIG = {
    "students_file": "students.csv",     # e.g. "Canteen_Dataset.csv"
    "menu_file": "menu.csv",              # e.g. "Canteen_Dataset1.csv"
    "orders_file": "orders.csv",          # e.g. "Canteen_Dataset2.csv"
    "feedback_file": "feedback.csv",      # e.g. "Canteen_Dataset3.csv"

    # Column names expected in each file — rename these strings
    # to match your CSV headers if they differ.
    "student_id_col": "student_id",
    "food_id_col": "food_id",
    "food_name_col": "food_name",
    "price_col": "price",
    "rating_col": "rating",

    "default_rating_for_unrated_orders": 3,  # neutral rating fallback
    "num_recommendations": 5,
}


# ============================================================
# 1. NLTK SETUP
# ============================================================

def ensure_nltk_data():
    """Download required NLTK resources if missing (silent, once)."""
    resources = [
        ("tokenizers/punkt", "punkt"),
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("corpora/wordnet", "wordnet"),
        ("corpora/omw-1.4", "omw-1.4"),
    ]
    for path, pkg in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(pkg, quiet=True)


lemmatizer = WordNetLemmatizer()

# Intents -> example/trigger words (lemmatized, lowercase).
# The bot lemmatizes whatever the user types and checks for overlap
# with these sets, so "eating", "eats", "ate" all match "eat".
INTENTS = {
    "greet": {"hi", "hello", "hey", "yo"},
    "recommend": {
        "recommend", "suggest", "eat", "food", "hungry", "menu",
        "order", "want", "craving", "starve",
    },
    "thanks": {"thanks", "thank", "great", "nice", "awesome"},
    "exit": {"exit", "quit", "bye", "goodbye", "stop"},
}


def lemmatize_message(message):
    """Tokenize + lemmatize a message into a set of base words."""
    tokens = word_tokenize(message.lower())
    lemmas = {lemmatizer.lemmatize(tok, pos="v") for tok in tokens if tok.isalpha()}
    return lemmas


def detect_intent(message):
    """Return the best-matching intent for a user message, or None."""
    lemmas = lemmatize_message(message)

    best_intent, best_overlap = None, 0
    for intent, trigger_words in INTENTS.items():
        overlap = len(lemmas & trigger_words)
        if overlap > best_overlap:
            best_intent, best_overlap = intent, overlap

    return best_intent


# ============================================================
# 2. LOAD DATA
# ============================================================

def load_data(config):
    try:
        students = pd.read_csv(config["students_file"])
        menu = pd.read_csv(config["menu_file"])
        orders = pd.read_csv(config["orders_file"])
        feedback = pd.read_csv(config["feedback_file"])
    except FileNotFoundError as e:
        print(f"\n❌ Could not find a required file: {e.filename}")
        print("   Check the file names in the CONFIG section at the "
              "top of this script.\n")
        sys.exit(1)

    return students, menu, orders, feedback


# ============================================================
# 3. CLEAN DATA
# ============================================================

def clean_data(orders, feedback, config):
    sid, fid, rcol = (
        config["student_id_col"],
        config["food_id_col"],
        config["rating_col"],
    )

    orders = orders.dropna(subset=[sid, fid]).copy()
    feedback = feedback.dropna(subset=[sid, fid, rcol]).copy()

    feedback[rcol] = pd.to_numeric(feedback[rcol], errors="coerce")
    feedback = feedback.dropna(subset=[rcol])

    return orders, feedback


# ============================================================
# 4. BUILD STUDENT-FOOD RATING MATRIX
# ============================================================

def build_rating_matrix(orders, feedback, config):
    sid, fid, rcol = (
        config["student_id_col"],
        config["food_id_col"],
        config["rating_col"],
    )

    rating_data = feedback.merge(
        orders[[sid, fid]].drop_duplicates(),
        on=[sid, fid],
        how="outer",
    )

    rating_data[rcol] = rating_data[rcol].fillna(
        config["default_rating_for_unrated_orders"]
    )

    rating_matrix = rating_data.pivot_table(
        index=sid,
        columns=fid,
        values=rcol,
        aggfunc="mean",
        fill_value=0,
    )

    return rating_matrix


# ============================================================
# 5. FOOD-TO-FOOD SIMILARITY
# ============================================================

def build_food_similarity(rating_matrix):
    if rating_matrix.empty:
        return pd.DataFrame()

    similarity = cosine_similarity(rating_matrix.T)

    return pd.DataFrame(
        similarity,
        index=rating_matrix.columns,
        columns=rating_matrix.columns,
    )


# ============================================================
# 6. RECOMMENDATION ENGINE
# ============================================================

def popular_foods(feedback, menu, config, n):
    """Fallback: top-rated foods overall (used for cold start)."""
    fid, rcol = config["food_id_col"], config["rating_col"]

    popular = (
        feedback.groupby(fid)[rcol]
        .mean()
        .sort_values(ascending=False)
        .head(n)
    )

    result = menu[menu[fid].isin(popular.index)].copy()
    result["rating"] = result[fid].map(popular)
    return result.sort_values("rating", ascending=False)


def recommend_food(student_id, rating_matrix, food_similarity_df,
                    feedback, menu, config):
    sid, fid = config["student_id_col"], config["food_id_col"]
    n = config["num_recommendations"]

    if student_id not in rating_matrix.index:
        return popular_foods(feedback, menu, config, n), "cold_start"

    student_ratings = rating_matrix.loc[student_id]
    liked_foods = student_ratings[student_ratings >= 4].index.tolist()

    if not liked_foods or food_similarity_df.empty:
        return popular_foods(feedback, menu, config, n), "no_likes"

    scores = {}
    for food in liked_foods:
        if food not in food_similarity_df.index:
            continue

        for similar_food, sim_score in food_similarity_df[food].items():
            if similar_food == food:
                continue
            if student_ratings.get(similar_food, 0) > 0:
                continue

            scores[similar_food] = scores.get(similar_food, 0) + sim_score

    if not scores:
        return popular_foods(feedback, menu, config, n), "no_scores"

    top_matches = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]
    recommended_ids = [food_id for food_id, _ in top_matches]

    result = menu[menu[fid].isin(recommended_ids)].copy()
    result["recommendation_score"] = result[fid].map(dict(top_matches))
    result = result.sort_values("recommendation_score", ascending=False)

    return result, "personalized"


# ============================================================
# 7. CHATBOT LOOP
# ============================================================

def print_recommendations(result, mode, config):
    name_col = config["food_name_col"]
    price_col = config["price_col"]

    if result.empty:
        print("Bot: Sorry, I couldn't find any recommendations right now.")
        return

    if mode == "cold_start":
        print("Bot: I don't know your taste yet, so here are some "
              "popular picks:\n")
    elif mode in ("no_likes", "no_scores"):
        print("Bot: I don't have enough of your ratings yet, so here "
              "are some popular picks:\n")
    else:
        print("Bot: Based on what you've liked before, try these:\n")

    for _, food in result.iterrows():
        name = food.get(name_col, "Unknown item")
        price = food.get(price_col, "N/A")
        print(f"  🍴 {name}  |  ₹{price}")
    print()


def run_chatbot(config):
    ensure_nltk_data()

    students, menu, orders, feedback = load_data(config)
    orders, feedback = clean_data(orders, feedback, config)
    rating_matrix = build_rating_matrix(orders, feedback, config)
    food_similarity_df = build_food_similarity(rating_matrix)

    print("====================================")
    print("     CANTEEN AI RECOMMENDER (NLTK)")
    print("====================================")

    student_id = input("Enter your Student ID: ").strip()

    print("\nBot: Hi! Ask me things like 'I'm hungry' or 'suggest "
          "some food'. Type 'exit' to quit.")

    while True:
        message = input("\nYou: ").strip()

        if not message:
            continue

        intent = detect_intent(message)

        if intent == "exit":
            print("Bot: Goodbye! 👋")
            break

        elif intent == "recommend":
            result, mode = recommend_food(
                student_id, rating_matrix, food_similarity_df,
                feedback, menu, config,
            )
            print_recommendations(result, mode, config)

        elif intent == "greet":
            print("Bot: Hello! Ask me to recommend some food 🙂")

        elif intent == "thanks":
            print("Bot: You're welcome! Let me know if you want more "
                  "suggestions.")

        else:
            print("Bot: I can recommend food based on your previous "
                  "orders and ratings. Try saying 'recommend food' "
                  "or 'I'm hungry'.")


# ============================================================
# 8. ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_chatbot(CONFIG)