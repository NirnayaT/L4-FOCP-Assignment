from src.interface.chat_window import ChatbotApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
