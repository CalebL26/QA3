import sqlite3
import tkinter as tk
from tkinter import ttk

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

    # Create a canvas to contain the questions and a scrollbar
    canvas = tk.Canvas(question_window)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(question_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the questions
    question_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=question_frame, anchor="nw")

    # Function to resize the canvas scroll region
    def resize_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    question_frame.bind("<Configure>", resize_scroll_region)

    
    def submit():
        user_answers = [option_vars[i].get() for i in range(len(option_vars))]
        correct_answers = [question[7] for question in questions if question[1] == selected_option]

        for i, (correct_answer) in enumerate(zip(correct_answers)):
            result_label = result_labels[i]
            result_label.config(text=f"Correct answer:{correct_answer}")


    option_vars = []  # Store option variables to access user selections later
    result_labels = []  # Store labels to display results after submission

    for question in questions:
        if question[1] == selected_option:
            question_text = question[2]
            options = [question[3], question[4], question[5], question[6]]
            answer = question[7]

            question_label = ttk.Label(question_frame, text=question_text)
            question_label.pack(padx=2, pady=2, anchor="w", fill="x")

            # Create option variables to store user selections
            option_var = tk.StringVar(value="")
            option_vars.append(option_var)

            for idx, option in enumerate(options):
                option_radio = ttk.Radiobutton(question_frame, text=option, value=option, variable=option_var)
                option_radio.pack(anchor="w")

            # Create label to display correct answer (initially hidden)
            correct_answer_label = ttk.Label(question_frame, text="Correct Answer: " + answer)
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
