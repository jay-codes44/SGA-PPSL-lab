from nltk.chat.util import Chat, reflections

PAIRS = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm doing well, thank you!", "I'm great, how about you?"]],
    [r"what is your name?", ["I'm a chatbot created by NLTK.", "You can call me NLTK Chatbot."]],
    [r"(.*)pizza(.*)", ["Pizza costs around $10 to $15 depending on the size and toppings."]],
    [r"(.*)time(.*)", ["The canteen is open from 9:00 AM to 5:00 PM.", "Canteen timings are 9:00 AM to 5:00 PM."]],
    [r"(.*)menu(.*)", ["Today's menu includes sandwiches, pizza, salads, and beverages.", "You can find the menu on the canteen's notice board."]],
    [r"quit", ["Goodbye!", "See  later!"]],
    [r"(.*)", ["The canteen is open from 9:00 AM to 5:00 PM."]],

]

chatbot = Chat(PAIRS, reflections)
chatbot.converse()