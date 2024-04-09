import sqlite3
import tkinter as tk
from tkinter import ttk

class Question:
    def __init__(self, category, text, options, correct_answer):
        self.category = category
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        formatted_question = f"{self.text}\n"
        for option in self.options:
            formatted_question += f"- {option}\n"
        return formatted_question


def on_option_selected(event):
    selected_option = dropdown.get()
    window.destroy()  # Close the first GUI window
    open_question_gui(selected_option)


def open_question_gui(selected_option):
    question_window = tk.Tk()
    question_window.title(selected_option + " Questions")

    conn = sqlite3.connect('business_questions.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    question_label = tk.Label(question_window, text="Answer the following questions:")
    question_label.pack()

    canvas = tk.Canvas(question_window)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(question_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    question_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=question_frame, anchor="nw")

    def resize_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    question_frame.bind("<Configure>", resize_scroll_region)

    def submit():
        user_answers = [option_vars[i].get() for i in range(len(option_vars))]
        correct_answers = [question.correct_answer for question in questions if question.category == selected_option]

        for i, (user_answer, correct_answer) in enumerate(zip(user_answers, correct_answers)):
            result_label = result_labels[i]
            if user_answer == correct_answer:
                result_label.config(text="Correct answer!")
            else:
                result_label.config(text=f"Incorrect. Correct answer: {correct_answer}")

    option_vars = []
    result_labels = []

    for question_data in questions:
        if question_data[1] == selected_option:
            category, text, options, correct_answer = question_data[1], question_data[2], question_data[3:7], question_data[7]
            question = Question(category, text, options, correct_answer)

            question_label = ttk.Label(question_frame, text=question.display_question())
            question_label.pack(padx=2, pady=2, anchor="w", fill="x")

            option_var = tk.StringVar(value="")
            option_vars.append(option_var)

            for idx, option in enumerate(question.options):
                option_radio = ttk.Radiobutton(question_frame, text=option, value=option, variable=option_var)
                option_radio.pack(anchor="w")

            result_label = ttk.Label(question_frame, text="")
            result_label.pack(anchor="w", pady=2)
            result_labels.append(result_label)

    submit_button = ttk.Button(question_window, text="Submit", command=submit)
    submit_button.pack(pady=5)

    score_label = tk.Label(question_window,text="")
    score_label.pack(pady=5)

    conn.close()

    question_window.mainloop()

window = tk.Tk()
window.title("Category Selector")

label = tk.Label(window, text="Welcome to the QuizBowl, please select a category you would like to be quizzed on...",
                 padx=100, pady=15, fg="white", bg="black", font=10)
label.pack()

options = ["Business Management", "Business Stats", "Database Management", "Marketing", "Business Application Development"]

dropdown = ttk.Combobox(window, values=options)
dropdown.pack()

dropdown.current(0)

dropdown.bind("<<ComboboxSelected>>", on_option_selected)

window.mainloop()
