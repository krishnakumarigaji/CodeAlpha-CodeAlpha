"""
TASK 4: Basic Chatbot
-----------------------
A simple rule-based chatbot that responds to a fixed set of inputs.

Concepts used: if-elif, functions, loops, input/output
"""


def get_response(user_input):
    """
    Return a predefined reply based on keywords found in the user's input.
    Using if-elif so the first matching rule wins.
    """
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm a simple rule-based chatbot built in Python."

    elif "help" in text:
        return "I can chat about basic greetings. Try saying 'hello', 'how are you', or 'bye'."

    elif "thank" in text:
        return "You're welcome!"

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Try saying 'hello', 'how are you', or 'help'."


def chat():
    print("=" * 40)
    print("Simple Chatbot (type 'bye' to exit)")
    print("=" * 40)

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        print("Bot:", response)

        # End the loop once the bot has said goodbye
        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()