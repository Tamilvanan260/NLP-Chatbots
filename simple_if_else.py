print("Bot : Hello! type 'bye' to exit.")

style = input("Choose bot style (funny / professional / friendly): ").lower()

while True:
    user_input = input(" ").lower()

    if user_input in ["hi", "hello"]:
        if style == "funny":
            print("Bot: Heyyy human! What's up?")
        elif style == "professional":
            print("Bot: Hello. How may I assist you today?")
        else:  
            print("Bot: Hi there! Nice to see you!")

    elif user_input == "how are you":
        if style == "funny":
            print("Bot: I'm doing great! Still waiting for my coffee.")
        elif style == "professional":
            print("Bot: I am functioning optimally. Thank you for asking.")
        else:
            print("Bot: I'm good! Thanks for asking.")

    elif user_input == "your name":
        if style == "funny":
            print("Bot: I'm Botman, protector of chats!")
        elif style == "professional":
            print("Bot: I am a simple rule-based chatbot.")
        else:
            print("Bot: I'm your friendly chatbot.")

    elif user_input == "what can you do":
        if style == "funny":
            print("Bot: I chat, I joke, I exist.")
        elif style == "professional":
            print("Bot: I can respond to predefined user inputs.")
        else:
            print("Bot: I can chat with you and answer simple questions!")

    elif user_input == "thanks":
        if style == "funny":
            print("Bot: You're welcome. Pay me in cookies.")
        elif style == "professional":
            print("Bot: You're welcome. Happy to help.")
        else:
            print("Bot: Anytime!")

    elif user_input == "bye":
        if style == "funny":
            print("Bot: Byeeee! Don't forget me.")
        elif style == "professional":
            print("Bot: Goodbye. Have a great day.")
        else:
            print("Bot: Bye! Take care.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
