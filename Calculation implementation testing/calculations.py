import tkinter as tk
from tkinter import ttk
import sqlite3

def calculate_overall_grade(course_name, course_weights):
    # Your existing code for calculating the overall grade

    def show_course_grade_and_assignments(course_name):
    # Create a new tkinter window
        course_window = tk.Toplevel()
        course_window.title(f"Course Grade and Assignments - {course_name}")

    # Fetch course weights
        course_weights = {'exam_weight': 40, 'project_weight': 20, 'quiz_weight': 10, 'homework_weight': 15, 'assignment_weight': 15}  # Example weights, you need to fetch these from somewhere
    
    # Calculate overall grade
        overall_grade = calculate_overall_grade(course_name, course_weights)

    # Create label to display overall grade
        grade_label = tk.Label(course_window, text=f"The overall grade for {course_name} is: {overall_grade:.2f}")
        grade_label.pack()

    # Create a treeview to display assignments
        assignments_tree = ttk.Treeview(course_window, columns=("Type", "Assignment Name", "Grade"), show="headings")
        assignments_tree.heading("Type", text="Type")
        assignments_tree.heading("Assignment Name", text="Assignment Name")
        assignments_tree.heading("Grade", text="Grade")
        assignments_tree.pack()

    # Populate the assignments tree
        db_file = f"{course_name.replace(' ', '_')}/{course_name.replace(' ', '_')}_assignments.db"
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assignments")
        assignments = cursor.fetchall()
        for assignment in assignments:
            assignments_tree.insert("", "end", values=assignment[1:])

        conn.close()
