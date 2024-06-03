# Rule-based chatbot implementation

def chatbot_response(user_input):
    # Convert the input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()
    
    # Define a set of rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm a chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Chatbot: Hi! I'm here to help you. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
