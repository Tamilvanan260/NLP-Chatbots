import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)

print("NLP Chatbot Started (type 'bye' to exit)")

how_words = ["how", "how's", "howdy"]
you_words = ["you", "u"]

while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot: Bye bro")
        break

    words = word_tokenize(user)

    if "hi" in words or "hello" in words:
        print("Bot: Hello bro")
    elif "name" in words:
        print("Bot: I'm an NLP chatbot ")
    elif any(h in words for h in how_words) and any(y in words for y in you_words):
        print("Bot: I'm doing great ")
    else:
        print("Bot: Sorry, I didn't understand ")
