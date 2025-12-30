import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)

print("NLP Chatbot Started (type 'bye' to exit)")

while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot: Bye bro")
        break

    words = word_tokenize(user)

    if "hi" in words or "hello" in words:
        print("Bot: Hello bro ")
    elif "name" in words:
        print("Bot: I'm an NLP chatbot ")
    elif "how" in words and "you" in words:
        print("Bot: I'm doing great ")
    else:
        print("Bot: Sorry, I didn't understand ")
