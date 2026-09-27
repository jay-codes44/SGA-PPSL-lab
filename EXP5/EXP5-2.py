# PRN : 2607012272
# name : jay mangukiya
# batch : C3hoi
from nltk.chat.util import Chat, reflections
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],

    [r"(.*) my name is (.*)", ["Hello %2! How can I assist you?"]],

    [r"(.*) your name\?", ["I am your friendly chatbot."]],

    [r"(.*) issue", ["The product is damaged."]],

    [r"(.*) refund", ["Please tell me the serial number."]],

    [r"(.*) serial number", ["Thank you for providing the serial number."]],

    [r"(.*) return", ["The product cannot be refunded."]],

    [r"(.*) product", ["The product will be replaced."]],

    [r"bye|exit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["You said: %1"]]
]

custom_reflections = reflections.copy()
custom_reflections.update({
    "we": "you all",
    "ours": "yours",
    "us": "you",
    "are you": "am i",
    "can i": "can you",
    "will you": "will i",
    "you": "your"
})


chatbot = Chat(pairs, custom_reflections)
chatbot.converse()