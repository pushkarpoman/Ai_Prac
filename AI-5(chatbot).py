print("BOT: Hello! I am your assistant bot.")
print("BOT: Type 'exit' anytime to end the chat.")

while True:
    user = input("You: ")
    user = user.lower()

    if user == "hi" or user == "hello":
        print("BOT: Hello! How can I assist you?")
    elif "name" in user:
        print("BOT: I am ChatBot, your virtual assistant.")
    elif "how are you" in user:
        print("BOT: I'm fine, thank you! How about you?")
    elif "book" in user and "flight" in user:
        print("BOT: Sure! Your flight is booked.")
    elif "thank" in user:
        print("BOT: You're welcome!")
    elif user == "exit":
        print("BOT: Goodbye! Have a nice day.")
        break
    else:
        print("BOT: Sorry, I didn't understand that.")
