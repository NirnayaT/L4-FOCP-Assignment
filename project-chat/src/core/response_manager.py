import json
from ..utils.config_loader import ConfigLoader

class ResponseManager:
    def __init__(self):
        self.config_loader = ConfigLoader()
        self.responses = self.config_loader.load_responses()

    def get_response(self, keyword, user_name):
        """Get appropriate response for the given keyword"""
        keyword = keyword.lower()
        if keyword in self.responses:
            return self.format_response(self.responses[keyword], user_name)
        return self.get_default_response(user_name)

    def format_response(self, response, user_name):
        """Format response with user name and any other placeholders"""
        return response.replace("{user_name}", user_name)

    def get_default_response(self, user_name):
        """Return a default response when no keyword match is found"""
        return f"I understand your interest, {user_name}. Could you please be more specific about what you'd like to know?"

    def get_quick_responses(self):
        """Get list of quick response options"""
        return [
            "Courses", "Fees", "Accommodation",
            "Library", "Sports", "Events"
        ]

    def update_responses(self, new_responses):
        """Update response dictionary with new responses"""
        self.responses.update(new_responses)
