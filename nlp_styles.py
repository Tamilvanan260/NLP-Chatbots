import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)

print("Bot: Hello! Type 'bye' to exit.")
style = input("Choose bot style (funny / professional / friendly): ").lower()

how_words = ["how", "how's", "howdy"]
you_words = ["you", "u"]

while True:
    user_input = input("You: ").lower()
    
    if user_input == "bye":
        if style == "funny":
            print("Bot: Byeeee! Don't forget me ")
        elif style == "professional":
            print("Bot: Goodbye. Have a great day!")
        else:
            print("Bot: Bye! Take care ")
        break

    words = word_tokenize(user_input)

    if "hi" in words or "hello" in words:
        if style == "funny":
            print("Bot: Heyyy human! What's up?")
        elif style == "professional":
            print("Bot: Hello. How may I assist you today?")
        else:
            print("Bot: Hi there! Nice to see you!")
    elif "name" in words:
        if style == "funny":
            print("Bot: I'm Botman, protector of chats!")
        elif style == "professional":
            print("Bot: I am a simple NLP chatbot.")
        else:
            print("Bot: I'm your friendly chatbot.")
    elif any(h in words for h in how_words) and any(y in words for y in you_words):
        if style == "funny":
            print("Bot: I'm doing great! Still waiting for coffee ")
        elif style == "professional":
            print("Bot: I am functioning optimally. Thank you for asking.")
        else:
            print("Bot: I'm good! Thanks for asking ")
    else:
        print("Bot: Sorry, I didn't understand ")
