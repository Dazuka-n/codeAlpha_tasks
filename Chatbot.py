import nltk
from nltk.chat.util import Chat, reflections

# Predefined patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you?"]],
    [r"what is your name?", ["I'm a chatbot created to assist you. You can call me ChatBot!"]],
    [r"how are you?", ["I'm just a program, but I'm functioning as expected! How about you?"]],
    [r"what can you do?", ["I can answer simple questions, have basic conversations, and assist with tasks."]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm not sure I understand that. Can you rephrase?"]],
]

# Reflective dictionary for dynamic responses
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Chatbot instance
def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
     # Ensure NLTK dependencies are downloaded
    chatbot()