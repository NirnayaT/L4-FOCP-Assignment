import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Database Storage System")

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

name_label = tk.Label(frame, text="Name")
name_label.grid(row=0, column=0, pady=10)

age_label = tk.Label(frame, text="Age")
age_label.grid(row=1, column=0, pady=10)

name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, columnspan=2)

age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1, columnspan=2)


def save_data():
    pass


save_button = tk.Button(frame, text="Save Button", command=save_data)
save_button.grid(row=2, column=1)


column = ("name", "age")
table = ttk.Treeview(frame, columns=column, show="headings")
table.heading("name", text="Name")
table.heading("age", text="Age")

table.column("name", anchor="center", width=100)
table.column("age", anchor="center", width=100)
table.grid(row = 2, column=0)
root.mainloop()
