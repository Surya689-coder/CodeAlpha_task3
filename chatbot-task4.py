def quizzy_chatbot():
    print("Quizzy: Hello! I'm Quizzy, your chat companion. Type something (type 'exit' to quit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Quizzy: Hey there!")
        elif user_input == "how are you":
            print("Quizzy: I'm doing great, thanks! How about you?")
        elif user_input == "bye":
            print("Quizzy: Goodbye! Talk to you later.")
        elif user_input == "what's your name" or user_input == "who are you":
            print("Quizzy: I'm Quizzy — your friendly chatbot with answers!")
        elif user_input == "thank you":
            print("Quizzy: You're most welcome!")
        elif user_input == "what can you do":
            print("Quizzy: I can chat, answer simple questions, and make your day better.")
        elif user_input == "exit":
            print("Quizzy: Chat ended. See you next time!")
            break
        else:
            print("Quizzy: Hmm, I didn't get that. Try asking something else.")

# Start the chatbot
quizzy_chatbot()