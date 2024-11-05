import nltk
import random
import string
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
            "how are you": ["I'm a bot, but thanks for asking!", "I'm here to help you!"],
            "bye": ["Goodbye!", "See you later!", "Have a great day!"],
            "default": ["I'm not sure I understand. Could you rephrase that?"]
        }

    def preprocess_input(self, user_input):
        user_input = user_input.lower()
        tokens = word_tokenize(user_input)
        tokens = [word for word in tokens if word not in stopwords.words('english') and word.isalnum()]
        return tokens

    def find_best_match(self, tokens):
        for token in tokens:
            for key in self.responses.keys():
                if key in token:
                    return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def chat(self):
        print("Chatbot: Hello! How can I help you today? Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["bye", "exit"]:
                print("Chatbot:", random.choice(self.responses["bye"]))
                break

            tokens = self.preprocess_input(user_input)
            response = self.find_best_match(tokens)
            print("Chatbot:", response)

# Usage
bot = SimpleChatbot()
bot.chat()
