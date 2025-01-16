import tkinter as tk
from ..utils.logger import Logger

class DialogManager:
    def __init__(self, chat_app):
        self.chat_app = chat_app
        self.logger = Logger()

    def show_name_dialog(self):
        dialog = tk.Toplevel(self.chat_app.root)
        dialog.title("Welcome to University of Poppleton")
        
        # Center the dialog
        window_width = 400
        window_height = 200
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))
        dialog.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Configure dialog
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.chat_app.root)
        dialog.grab_set()
        
        # Welcome message
        tk.Label(
            dialog,
            text="Welcome to our Virtual Chatbot!",
            font=("Helvetica", 14, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=(20,10))
        
        tk.Label(
            dialog,
            text="Please enter your name:",
            font=("Helvetica", 11),
            bg='#f0f0f0',
            fg='#2c3e50'
        ).pack(pady=(0,10))
        
        # Name entry
        name_var = tk.StringVar()
        entry = tk.Entry(
            dialog,
            textvariable=name_var,
            font=("Helvetica", 12),
            width=30,
            relief=tk.FLAT,
            bg='white'
        )
        entry.pack(pady=10, ipady=8)
        entry.focus()
        
        # Submit button
        submit_btn = tk.Button(
            dialog,
            text="Start Chatting",
            command=lambda: self.submit_name(name_var.get(), dialog),
            font=("Helvetica", 11, "bold"),
            bg='#2c3e50',
            fg='white',
            padx=40,
            height=2
        )
        submit_btn.pack(pady=20)
        
        # Bind Enter key
        entry.bind('<Return>', lambda e: self.submit_name(name_var.get(), dialog))

    def submit_name(self, name, dialog):
        if name.strip():
            self.chat_app.user_name = name.strip()
        else:
            self.chat_app.user_name = "Guest"
        
        dialog.destroy()
        welcome_message = f"Hello, {self.chat_app.user_name}! How can I help you with your questions about the University of Poppleton?"
        self.chat_app.display_message(welcome_message, is_agent=True)

    def start_welcome_tour(self):
        tour_messages = [
            "Welcome to the University of Poppleton's virtual tour!",
            "I can help you with information about courses, accommodation, and campus life.",
            "Try clicking the quick response buttons below for common topics.",
            "Or simply type your question and I'll be happy to help!",
            "Let's begin - what would you like to know about Poppleton?"
        ]
        
        for i, msg in enumerate(tour_messages):
            self.chat_app.root.after(i * 1500, lambda m=msg: self.chat_app.display_message(m, is_agent=True))
