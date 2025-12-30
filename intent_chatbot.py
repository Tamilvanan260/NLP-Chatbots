import nltk
from nltk.tokenize import word_tokenize
import random
from datetime import datetime

nltk.download('punkt', quiet=True)

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey"],
        "responses": ["Hello!", "Hey there!", "Hi! How can I help?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": ["Bye! Take care", "Goodbye!", "See you soon!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": ["You're welcome", "No problem!", "Anytime!"]
    },
    "name": {
        "patterns": ["name", "who are you"],
        "responses": ["I'm your NLP chatbot", "I am a simple chatbot"]
    },
    "how": {
        "patterns": ["how are you", "how r u"],
        "responses": ["I'm doing great", "I am fine! How about you?"]
    },
    "time": {
        "patterns": ["time", "current time"],
        "responses": []  # handled dynamically
    },
    "date": {
        "patterns": ["date", "today"],
        "responses": []  # handled dynamically
    },
    "joke": {
        "patterns": ["joke", "funny"],
        "responses": [
            "Why did the computer catch a cold? Because it left its Windows open.",
            "Why do programmers love dark mode? Because light attracts bugs.",
            "Why was the computer tired? It worked all day!"
        ]
    },
    "help": {
        "patterns": ["help", "what can you do", "commands"],
        "responses": [
            "I can greet you, tell my name, respond to thanks, tell time, date, and crack a joke."
        ]
    }
}

print("Advanced NLP Chatbot Started (type 'bye' to exit)")
print("Type 'help' to see what I can do")

while True:
    user_input = input("You: ").lower()
    words = word_tokenize(user_input)

    if user_input in ["bye", "goodbye"]:
        print(random.choice(intents["goodbye"]["responses"]))
        break

    matched = False

    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_words = word_tokenize(pattern)
            if any(w in words for w in pattern_words):

                # Dynamic responses
                if intent == "time":
                    print("Current time:", datetime.now().strftime("%H:%M:%S"))
                elif intent == "date":
                    print("Today's date:", datetime.now().strftime("%d-%m-%Y"))
                else:
                    print(random.choice(data["responses"]))

                matched = True
                break
        if matched:
            break

    if not matched:
        print("Bot: Sorry, I didn't understand. Type 'help' to see options.")

