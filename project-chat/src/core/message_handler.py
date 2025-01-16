import random
from ..utils.config_loader import ConfigLoader
from ..utils.logger import Logger

class MessageHandler:
    def __init__(self):
        self.config_loader = ConfigLoader()
        self.logger = Logger()
        self.responses = self.config_loader.load_responses()
        self.agent_name = self.config_loader.get_random_agent_name()

    def process_message(self, user_input, user_name):
        # Log the user message
        self.logger.log_session(user_input, "")

        # Check for exit commands
        if self.is_exit_command(user_input):
            return self.get_farewell_message(user_name), True

        # Check for disconnection
        if self.simulate_disconnection():
            return "*Connection Lost* Please refresh the chat.", True

        # Get response
        response = self.detect_keywords(user_input, user_name)
        
        # Log the response
        self.logger.log_session(user_input, response)
        
        return response, False

    def detect_keywords(self, user_input, user_name):
        user_input = user_input.lower()
        for keyword, response in self.responses.items():
            if keyword in user_input:
                return response.replace("{user_name}", user_name)
        return self.get_random_response(user_name)

    def get_random_response(self, user_name):
        responses = [
            f"That's an interesting point, {user_name}! Could you tell me more?",
            "I'm not quite sure about that. Could you rephrase?",
            f"Thanks for asking, {user_name}. Let me check that for you.",
            "That's a great question! Let me find the best information for you.",
            f"I appreciate your interest, {user_name}. Could you be more specific?"
        ]
        return random.choice(responses)

    def is_exit_command(self, text):
        exit_commands = ["bye", "quit", "exit", "goodbye"]
        return any(cmd in text.lower() for cmd in exit_commands)

    def get_farewell_message(self, user_name):
        return f"Goodbye {user_name}! Thank you for chatting with us today!"

    def simulate_disconnection(self):
        return random.random() < 0.05
