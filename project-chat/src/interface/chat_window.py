import tkinter as tk
from tkinter import scrolledtext
from .dialog_manager import DialogManager
from .style_config import StyleConfig
from ..core.message_handler import MessageHandler
from ..core.response_manager import ResponseManager
from ..core.session_manager import SessionManager
from ..utils.logger import Logger
import datetime

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.style = StyleConfig()
        self.dialog_manager = DialogManager(self)
        self.message_handler = MessageHandler()
        self.response_manager = ResponseManager()
        self.session_manager = SessionManager()
        self.logger = Logger()
        
        self.setup_window()
        self.create_widgets()
        self.start_session()

    def setup_window(self):
        self.style.configure_window(self.root)
        
    def create_widgets(self):
        self.create_header()
        self.create_chat_history()
        self.create_input_area()
        self.create_quick_buttons()
        self.create_status_bar()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg=self.style.colors['primary'])
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.header = tk.Label(
            header_frame,
            text=f"Welcome to University of Poppleton!\nI am {self.message_handler.agent_name}, your virtual assistant.",
            **self.style.get_header_style()
        )
        self.header.pack(fill=tk.X)

    def create_chat_history(self):
        self.chat_history = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            height=20,
            **self.style.get_input_style()
        )
        self.chat_history.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.chat_history.configure(state="disabled")

    def create_input_area(self):
        input_frame = tk.Frame(self.root, bg=self.style.colors['background'])
        input_frame.pack(fill=tk.X, pady=(0, 10))

        self.user_input = tk.Entry(
            input_frame,
            **self.style.get_input_style()
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            **self.style.get_button_style()
        )
        self.send_button.pack(side=tk.RIGHT, padx=(10, 0))

    def create_quick_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.style.colors['background'])
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        quick_responses = self.response_manager.get_quick_responses()
        for response in quick_responses:
            btn = tk.Button(
                button_frame,
                text=response,
                command=lambda x=response: self.quick_response(x),
                **self.style.get_button_style()
            )
            btn.pack(side=tk.LEFT, padx=5)

    def create_status_bar(self):
        self.status_bar = tk.Label(
            self.root,
            text="",
            bd=1,
            relief=tk.FLAT,
            font=self.style.fonts['normal'],
            bg=self.style.colors['primary'],
            fg=self.style.colors['white'],
            anchor=tk.W,
            padx=10,
            pady=5
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_session(self):
        self.dialog_manager.show_name_dialog()
        self.dialog_manager.start_welcome_tour()

    def display_message(self, message, is_agent=True):
        self.chat_history.configure(state="normal")
        
        timestamp = datetime.datetime.now().strftime("%H:%M")
        self.chat_history.insert(tk.END, f"[{timestamp}] ", "time")
        
        sender = f"{self.message_handler.agent_name}: " if is_agent else f"{self.user_name}: "
        tag = "agent" if is_agent else "user"
        self.chat_history.insert(tk.END, sender, tag)
        
        self.chat_history.insert(tk.END, message + "\n\n")
        
        self.chat_history.tag_config("time", foreground="gray")
        self.chat_history.tag_config("agent", foreground="blue")
        self.chat_history.tag_config("user", foreground="green")
        
        self.chat_history.configure(state="disabled")
        self.chat_history.see(tk.END)

    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return

        self.display_message(user_text, is_agent=False)
        self.session_manager.increment_message_count()
        
        response, should_exit = self.message_handler.process_message(user_text, self.user_name)
        
        if should_exit:
            self.root.after(1500, self.root.quit)
        else:
            self.show_typing_status()
            self.root.after(1000, lambda: self.display_message(response, is_agent=True))
        
        self.user_input.delete(0, tk.END)

    def quick_response(self, topic):
        self.user_input.delete(0, tk.END)
        self.user_input.insert(0, topic)
        self.send_message()

    def show_typing_status(self):
        self.status_bar.config(text=f"{self.message_handler.agent_name} is typing...")
        self.root.after(1000, lambda: self.status_bar.config(text=""))
