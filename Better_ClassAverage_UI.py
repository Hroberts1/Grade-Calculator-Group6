# Python program to create a table

import tkinter as tk

def on_button_click():
    # This function will be called when the "Class Average" button is clicked
    # Create and display the pop-up window for adding a course
    create_needed_grade_popup()



def create_needed_grade_popup():
    # Create the pop-up window
    popup = tk.Toplevel()

    # Create labels and entry widgets for course name and weights
    assignment_label = tk.Label(popup, text="Assignment Average:")
    assignment_label.grid(row=0, column=0, padx=10, pady=5)
    assignment_average = tk.Label(popup, text="90")
    assignment_average.grid(row=0, column=1, padx=10, pady=5)

    homework_label = tk.Label(popup, text="Homework Average:")
    homework_label.grid(row=1, column=0, padx=10, pady=5)
    homework_average = tk.Label(popup, text="95")
    homework_average.grid(row=1, column=1, padx=10, pady=5)

    quiz_label = tk.Label(popup, text="Quiz Average:")
    quiz_label.grid(row=2, column=0, padx=10, pady=5)
    quiz_average = tk.Label(popup, text="80")
    quiz_average.grid(row=2, column=1, padx=10, pady=5)

    exam_label = tk.Label(popup, text="Exam Average:")
    exam_label.grid(row=3, column=0, padx=10, pady=5)
    exam_average = tk.Label(popup, text="92")
    exam_average.grid(row=3, column=1, padx=10, pady=5)

    class_label = tk.Label(popup, text="Class Average:")
    class_label.grid(row=3, column=0, padx=10, pady=5)
    class_average = tk.Label(popup, text="92")
    class_average.grid(row=3, column=1, padx=10, pady=5)

    # Create and place the back button
    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


# Create the main application window
root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("750x750")

button = tk.Button(root, text="Class Average", command=on_button_click, width=15, height=2)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
