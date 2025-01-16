import json
import random
import os

class ConfigLoader:
    def __init__(self):
        self.config_directory = "config"
        self.responses_file = os.path.join(self.config_directory, "responses.json")
        self.agents_file = os.path.join(self.config_directory, "agents.txt")
        self.ui_config_file = os.path.join(self.config_directory, "ui_config.json")

    def load_responses(self):
        """Load response configurations from JSON file"""
        try:
            with open(self.responses_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return self.get_default_responses()

    def get_random_agent_name(self):
        """Get a random agent name from the agents file"""
        try:
            with open(self.agents_file, 'r', encoding='utf-8') as file:
                names = [line.strip() for line in file.readlines()]
            return random.choice(names)
        except FileNotFoundError:
            return "Assistant"

    def load_ui_config(self):
        """Load UI configuration settings"""
        try:
            with open(self.ui_config_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return self.get_default_ui_config()

    def get_default_responses(self):
        """Return default responses if config file is not found"""
        return {
            "hello": "Hi {user_name}! How can I help you today?",
            "bye": "Goodbye {user_name}! Have a great day!",
            "help": "I can help you with information about courses, fees, and campus life."
        }

    def get_default_ui_config(self):
        """Return default UI configuration"""
        return {
            "colors": {
                "primary": "#2c3e50",
                "secondary": "#34495e",
                "background": "#f0f0f0"
            },
            "fonts": {
                "header": "Helvetica 14 bold",
                "normal": "Helvetica 11",
                "button": "Helvetica 11 bold"
            }
        }
