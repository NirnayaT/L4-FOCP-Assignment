import datetime
from ..utils.logger import Logger

class SessionManager:
    def __init__(self):
        self.logger = Logger()
        self.session_start_time = datetime.datetime.now()
        self.user_name = None
        self.agent_name = None
        self.is_active = False
        self.message_count = 0

    def start_session(self, user_name, agent_name):
        self.user_name = user_name
        self.agent_name = agent_name
        self.is_active = True
        self.session_start_time = datetime.datetime.now()
        self.log_session_start()

    def end_session(self):
        if self.is_active:
            self.is_active = False
            self.log_session_end()
            return f"Goodbye {self.user_name}! Thank you for chatting with us today!"
        return None

    def log_session_start(self):
        start_message = f"Session started with {self.user_name} at {self.session_start_time}"
        self.logger.log_session("SYSTEM", start_message)

    def log_session_end(self):
        duration = datetime.datetime.now() - self.session_start_time
        end_message = f"Session ended. Duration: {duration}. Messages: {self.message_count}"
        self.logger.log_session("SYSTEM", end_message)

    def increment_message_count(self):
        self.message_count += 1

    def get_session_duration(self):
        return datetime.datetime.now() - self.session_start_time

    def is_session_active(self):
        return self.is_active
