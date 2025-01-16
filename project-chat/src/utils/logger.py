import datetime
import os

class Logger:
    def __init__(self):
        self.log_directory = "logs/chat_logs"
        self.ensure_log_directory_exists()
        self.current_log_file = self.create_log_file()

    def ensure_log_directory_exists(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

    def create_log_file(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{self.log_directory}/chat_session_{timestamp}.txt"

    def log_session(self, user_input, response):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.current_log_file, "a", encoding='utf-8') as log_file:
            log_file.write(f"[{timestamp}] User: {user_input}\n")
            if response:
                log_file.write(f"[{timestamp}] Bot: {response}\n")
            log_file.write("-" * 50 + "\n")

    def log_system_message(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.current_log_file, "a", encoding='utf-8') as log_file:
            log_file.write(f"[{timestamp}] SYSTEM: {message}\n")
            log_file.write("-" * 50 + "\n")
