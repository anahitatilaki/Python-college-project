"""
Math Game: A GUI program to help kids learn multiplication tables.
Anahita Tilaki
Date: 12/8/2024
"""

import tkinter as tk
from tkinter import ttk
import random

class MathGame:
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("Math Game")

        # Variables for mode, question, and user input
        self.mode = tk.StringVar(value="Quiz")
        self.num1 = 0
        self.num2 = 0
        self.user_answer = tk.StringVar()
        self.answer_label_text = tk.StringVar(value="")
        self.question_text = tk.StringVar(value="")

        # Set up GUI widgets
        self.create_widgets()
        self.generate_question()
        
        self.window.mainloop()

    def create_widgets(self):
        """Create and arrange widgets in the GUI."""
        # Mode selection
        mode_frame = ttk.LabelFrame(self.window, text="Mode")
        mode_frame.grid(row=0, column=0, padx=10, pady=10)
        ttk.Radiobutton(mode_frame, text="Quiz Mode", variable=self.mode, value="Quiz", command=self.process_mode).grid(row=0, column=0)
        ttk.Radiobutton(mode_frame, text="FlashCard Mode", variable=self.mode, value="FlashCard", command=self.process_mode).grid(row=0, column=1)

        # Question and Answer Frame
        qa_frame = ttk.Frame(self.window)
        qa_frame.grid(row=1, column=0, padx=10, pady=10)
        self.question_label = ttk.Label(qa_frame, textvariable=self.question_text, font=("Arial", 14))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(qa_frame, text="Your Answer:").grid(row=1, column=0, padx=5, pady=5)
        self.answer_entry = ttk.Entry(qa_frame, textvariable=self.user_answer)
        self.answer_entry.grid(row=1, column=1, padx=5, pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)
        self.answer_label = ttk.Label(qa_frame, textvariable=self.answer_label_text, font=("Arial", 12))
        self.answer_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(button_frame, text="Show Answer", command=self.show_answer).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Next Question", command=self.next_question).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Exit Game", command=self.window.destroy).grid(row=0, column=2, padx=5)

    def process_mode(self):
        """Switch between Quiz and FlashCard mode."""
        if self.mode.get() == "FlashCard":
            self.answer_entry.grid_remove()
            self.answer_label.grid_remove()
        else:
            self.answer_entry.grid()
            self.answer_label.grid()

    def generate_question(self):
        """Generate a new multiplication question."""
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        self.question_text.set(f"What is {self.num1} x {self.num2}?")
        self.answer_label_text.set("")
        self.user_answer.set("")

    def check_answer(self, event=None):
        """Check if user's answer is correct."""
        try:
            user_answer = int(self.user_answer.get())
            correct_answer = self.num1 * self.num2
            if user_answer == correct_answer:
                self.answer_label_text.set("Correct! Great job!")
            else:
                self.answer_label_text.set(f"Incorrect! The correct answer is {correct_answer}.")
        except ValueError:
            self.answer_label_text.set("Please enter a valid number.")

    def show_answer(self):
        """Display the correct answer."""
        correct_answer = self.num1 * self.num2
        self.answer_label_text.set(f"The correct answer is {correct_answer}.")

    def next_question(self):
        """Generate the next question."""
        self.generate_question()


# Run the Math Game
if __name__ == "__main__":
    MathGame()
