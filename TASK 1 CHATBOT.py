import random
from datetime import datetime
import re

class AdvancedChatbot:
    def __init__(self):
        self.user_name = None
        self.conversation_history = []

    def chatbot_response(self, user_input):
        user_input = user_input.lower()
        self.conversation_history.append(f"User: {user_input}")

        # Greeting responses
        if re.search(r'\b(hello|hi|hey)\b', user_input):
            response = self.greet()

        # Asking about the chatbot
        elif re.search(r'\b(who are you|what are you)\b', user_input):
            response = "I'm an advanced rule-based chatbot designed to assist you with various queries and tasks."

        # Asking for help
        elif "help" in user_input:
            response = "I can help with greetings, telling time, basic calculations, and answering questions about myself. What would you like assistance with?"

        # Asking about the weather
        elif "weather" in user_input:
            response = "I'm unable to check live weather, but I can suggest a reliable weather website if you'd like."

        # Asking about time
        elif "time" in user_input:
            response = self.get_time()

        # Basic calculations
        elif any(op in user_input for op in ['+', '-', '*', '/']):
            response = self.calculate(user_input)

        # Remembering user's name
        elif "my name is" in user_input:
            self.user_name = user_input.split("my name is")[-1].strip()
            response = f"Nice to meet you, {self.user_name}! I'll remember your name."

        # Asking for user's name
        elif "what's my name" in user_input:
            response = self.recall_name()

        # Asking for conversation history
        elif "conversation history" in user_input:
            response = self.get_conversation_history()

        # Default response for unrecognized queries
        else:
            response = "I'm not sure how to respond to that. Could you please rephrase or ask something else?"

        self.conversation_history.append(f"Chatbot: {response}")
        return response

    def greet(self):
        greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Greetings! How may I be of service?",
            "Hey! What's on your mind today?"
        ]
        return random.choice(greetings)

    def get_time(self):
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    def calculate(self, expression):
        try:
            result = eval(re.sub(r'[^0-9+\-*/().\s]', '', expression))
            return f"The result of the calculation is: {result}"
        except:
            return "Sorry, I couldn't perform that calculation. Please make sure it's a valid arithmetic expression."

    def recall_name(self):
        if self.user_name:
            return f"Your name is {self.user_name}."
        else:
            return "I'm sorry, but you haven't told me your name yet. You can tell me by saying 'My name is [Your Name]'."

    def get_conversation_history(self):
        if len(self.conversation_history) > 2:
            return "Here's a summary of our conversation:\n" + "\n".join(self.conversation_history[-6:])
        else:
            return "We haven't had much of a conversation yet. Feel free to chat more!"

def main():
    chatbot = AdvancedChatbot()
    print("Chatbot: Hello! I'm an advanced chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot.chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
