# PRN : 2607012272
# name : jay mangukiya
# batch : C3
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! What can I do for you today?", "Hi! How can I help you?"]],
    [r"my name is (.*)", ["Nice to meet you, %1! How may I help you?"]],
    [r"(.*) your name", ["I am your helpful chatbot!"]],
    [r"(.*) issue ", ["The product appears to be damaged"]],
    [r"(.*) refund ", ["Could you provide the serial number, please?"]],
    [r"(.*) serial number ", ["Thank you for providing the number"]],
    [r"(.*) Return", ["Unfortunately, the product cannot be refunded"]],
    [r"(.*) product ", ["The product will be r eplaced within the specified time"]],
    [r"bye", ["Goodbye! Enjoy the rest of your day!", "Until next time!"]],
    [r"(.*)", ["Sorry, I did not understand that. Could you please rephrase it?"]],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
