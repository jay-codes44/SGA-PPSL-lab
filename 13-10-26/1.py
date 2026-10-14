import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

df = pd.read_csv("SIT_Canteen_Google_Form_Feedback.csv")

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(feedback):
    score = sia.polarity_scores(feedback)["compound"]

    if score >= 0.05:
        sentiment = "Positive"
    elif score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return pd.Series([score, sentiment])

df[["Sentiment_Score", "Sentiment"]] = \
    df["Canteen_Feedback"].apply(analyze_sentiment)

print(df[[
    "Student_Staff_ID",
    "Canteen_Feedback",
    "Sentiment_Score",
    "Sentiment"
]])

df.to_csv("Canteen_Feedback_With_Sentiment.csv",
          index=False)

print("\nSentiment analysis completed.")

# Run the script
# Make sure the CSV file is in the same folder
# Output will include score and sentiment label

a