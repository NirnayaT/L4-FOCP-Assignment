import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Student Report Generator")


subjects = ["Science", "Mathematics", "Computer", "English"]
marks = {}

first_frame = tk.Frame(root)
first_frame.pack(padx=20, pady=10, side="top")


for i, subject in enumerate(subjects):
    marks[subject] = tk.IntVar(value=0)
    subject1_label = tk.Label(first_frame, text=f"Mark of {subjects[i]}:")
    subject1_label.grid(row=i, column=0, padx=30, sticky="w")

    subject1_entry = tk.Entry(first_frame, textvariable=marks[subject])
    subject1_entry.grid(row=i, column=1, sticky="w")

result_label = tk.Label(first_frame, text="Result", font=("Arial", 10, "underline"))
result_label.grid(row=4, column=0, columnspan=3, pady=10)

column = ("subject", "total_mark", "marks_obtained", "grade", "remarks")
tree = ttk.Treeview(first_frame, columns=column, show="headings")
tree.grid(row=5, column=0, padx=20, pady=10, columnspan=4)

tree.heading("subject", text="Subject")
tree.heading("total_mark", text="Total  Mark")
tree.heading("marks_obtained", text="Marks Obtained")
tree.heading("grade", text="Grade")
tree.heading("remarks", text="Remarks")

tree.column("subject", anchor="center", width=100)
tree.column("total_mark", anchor="center", width=100)
tree.column("marks_obtained", anchor="center", width=100)
tree.column("grade", anchor="center", width=100)
tree.column("remarks", anchor="center", width=100)


def gradeFinding(marks):
    if marks >= 90:
        return "A+"
    elif marks < 90 and marks >= 80:
        return "A"
    elif marks < 80 and marks >= 70:
        return "B+"
    elif marks < 70 and marks >= 60:
        return "B"
    elif marks < 60 and marks >= 50:
        return "C+"
    elif marks < 50 and marks >= 40:
        return "C"
    elif marks < 40 and marks >= 20:
        return "D"
    elif marks < 20 and marks >= 1:
        return "E"
    else:
        return "N"


def remarksFinding(grade):
    if grade == "A+":
        return "Outstanding"
    elif grade == "A":
        return "Excellent"
    elif grade == "B+":
        return "Very Good"
    elif grade == "B":
        return "Good"
    elif grade == "C+":
        return "Above Average"
    elif grade == "C":
        return "Average"
    elif grade == "D":
        return "Below Average"
    elif grade == "E":
        return "Poor"
    else:
        return "Not Graded"


def generate_report():
    total_mark = 100
    total_marks = 0
    for item in tree.get_children():
        tree.delete(item)
        print(item)

    for subject in subjects:
        mark = marks[subject].get()
        total_marks += mark
        grade = gradeFinding(mark)
        remarks = remarksFinding(grade)
        tree.insert("", tk.END, values=(subject, total_mark, mark, grade, remarks))

    percentage = (total_marks / (len(subjects) * 100)) * 100
    overall_grade = gradeFinding(percentage)
    percentage_value.config(text=f"{percentage}%")
    overall_grade_value.config(text=overall_grade)
    if percentage >= 50:
        result_value.config(text="Pass", fg="green")
    else:
        result_value.config(text="Fail", fg="red")


percentage_label = tk.Label(first_frame, text="Percentage:")
percentage_label.grid(row=6, column=0, pady=10)

percentage_value = tk.Label(first_frame, text="")
percentage_value.grid(row=6, column=1, pady=10)


overall_grade_label = tk.Label(first_frame, text="Overall Grade:")
overall_grade_label.grid(row=7, column=0, pady=10)

overall_grade_value = tk.Label(first_frame, text="")
overall_grade_value.grid(row=7, column=1, pady=10)

result_status = tk.Label(first_frame, text="Result:")
result_status.grid(row=8, column=0, pady=10)

result_value = tk.Label(first_frame, text="")
result_value.grid(row=8, column=1, pady=10)

tk.Button(first_frame, text="Generate Report", command=generate_report).grid(
    row=9, column=0, columnspan=3, padx=20, pady=10
)


root.mainloop()
