import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os
import sqlite3
from grade_calculator import calculate_exact_grade

courses = []
MAIN_DIRECTORY = "COURSES"

def fetch_courses_from_db():
    for root, dirs, files in os.walk(MAIN_DIRECTORY):
        for filename in files:
            if filename.endswith("_info.db"):
                course_name = filename.replace('_info.db', '').replace('_', ' ')
                courses.append({"course_name": course_name})

fetch_courses_from_db()

def on_button_click():
    create_add_course_popup()

def create_add_course_popup():
    popup = tk.Toplevel()
    popup.title("Add Course")

    course_name_label = tk.Label(popup, text="Course Name:")
    course_name_label.grid(row=0, column=0, padx=10, pady=5)
    course_name_entry = tk.Entry(popup)
    course_name_entry.grid(row=0, column=1, padx=10, pady=5)

    exam_weight_label = tk.Label(popup, text="Exam Weight (Ex: 40%):")
    exam_weight_label.grid(row=1, column=0, padx=10, pady=5)
    exam_weight_entry = tk.Entry(popup)
    exam_weight_entry.grid(row=1, column=1, padx=10, pady=5)

    project_weight_label = tk.Label(popup, text="Project Weight (Ex: 20%):")
    project_weight_label.grid(row=2, column=0, padx=10, pady=5)
    project_weight_entry = tk.Entry(popup)
    project_weight_entry.grid(row=2, column=1, padx=10, pady=5)

    quiz_weight_label = tk.Label(popup, text="Quiz Weight (Ex: 10%):")
    quiz_weight_label.grid(row=3, column=0, padx=10, pady=5)
    quiz_weight_entry = tk.Entry(popup)
    quiz_weight_entry.grid(row=3, column=1, padx=10, pady=5)

    homework_weight_label = tk.Label(popup, text="Homework Weight (Ex: 15%):")
    homework_weight_label.grid(row=4, column=0, padx=10, pady=5)
    homework_weight_entry = tk.Entry(popup)
    homework_weight_entry.grid(row=4, column=1, padx=10, pady=5)

    assignment_weight_label = tk.Label(popup, text="Assignment Weight (Ex: 15%):")
    assignment_weight_label.grid(row=5, column=0, padx=10, pady=5)
    assignment_weight_entry = tk.Entry(popup)
    assignment_weight_entry.grid(row=5, column=1, padx=10, pady=5)

    def submit_course():
        course_data = {
            "course_name": course_name_entry.get(),
            "exam_weight": exam_weight_entry.get(),
            "project_weight": project_weight_entry.get(),
            "quiz_weight": quiz_weight_entry.get(),
            "homework_weight": homework_weight_entry.get(),
            "assignment_weight": assignment_weight_entry.get()
        }
        courses.append(course_data)
        update_main_menu()
        
        course_directory = os.path.join(MAIN_DIRECTORY, course_data['course_name'].replace(' ', '_'))
        os.makedirs(course_directory, exist_ok=True)
        
        course_info_db = sqlite3.connect(os.path.join(course_directory, f"{course_data['course_name'].replace(' ', '_')}_info.db"))
        course_info_cursor = course_info_db.cursor()
        course_info_cursor.execute('''CREATE TABLE IF NOT EXISTS course_info
                                     (id INTEGER PRIMARY KEY,
                                     course_name TEXT,
                                     exam_weight TEXT,
                                     project_weight TEXT,
                                     quiz_weight TEXT,
                                     homework_weight TEXT,
                                     assignment_weight TEXT)''')
        course_info_cursor.execute('''INSERT INTO course_info
                                     (course_name, exam_weight, project_weight, quiz_weight, homework_weight, assignment_weight)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                     (course_data['course_name'], course_data['exam_weight'], course_data['project_weight'],
                                      course_data['quiz_weight'], course_data['homework_weight'], course_data['assignment_weight']))
        course_info_db.commit()
        course_info_db.close()

        popup.destroy()

    submit_button = tk.Button(popup, text="Submit", command=submit_course)
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def update_main_menu():
    for i, course in enumerate(courses):
        frame = tk.Frame(root)
        frame.grid(row=i+1, column=0, padx=10, pady=5)

        course_button = tk.Button(frame, text=course["course_name"], command=lambda c=course: on_course_button_click(root, c))
        course_button.grid(row=0, column=0)

def on_course_button_click(root, course):
    course_menu_window = tk.Toplevel(root)
    course_menu_window.title(f"Menu for {course['course_name']}")

    add_assignment_button = tk.Button(course_menu_window, text="Add Assignment", command=lambda: create_add_assignment_popup(course))
    add_assignment_button.pack()

    view_assignments_button = tk.Button(course_menu_window, text="View Assignments", command=lambda: view_assignments(course))
    view_assignments_button.pack()

    calculate_grade_button = tk.Button(course_menu_window, text="Calculate Average Grade", command=lambda: calculate_grade(course))
    calculate_grade_button.pack()

def create_add_assignment_popup(course):
    popup = tk.Toplevel()
    popup.title("Add Assignment")

    assignment_name_label = tk.Label(popup, text="Assignment Name:")
    assignment_name_label.grid(row=0, column=0, padx=10, pady=5)
    assignment_name_entry = tk.Entry(popup)
    assignment_name_entry.grid(row=0, column=1, padx=10, pady=5)

    grade_value_label = tk.Label(popup, text="Grade Value:")
    grade_value_label.grid(row=1, column=0, padx=10, pady=5)
    grade_value_entry = tk.Entry(popup)
    grade_value_entry.grid(row=1, column=1, padx=10, pady=5)

    weight_type_label = tk.Label(popup, text="Weight Type:")
    weight_type_label.grid(row=2, column=0, padx=10, pady=5)
    weight_types = ["Exam", "Project", "Quiz", "Homework", "Assignment"]
    weight_type_var = tk.StringVar()
    weight_type_var.set(weight_types[0])
    weight_type_dropdown = tk.OptionMenu(popup, weight_type_var, *weight_types)
    weight_type_dropdown.grid(row=2, column=1, padx=10, pady=5)

    def submit_assignment():
        assignment_data = {
            "assignment_name": assignment_name_entry.get(),
            "grade_value": grade_value_entry.get(),
            "weight_type": weight_type_var.get(),
        }
        assignments_db = sqlite3.connect(os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db"))
        assignments_cursor = assignments_db.cursor()
        assignments_cursor.execute('''CREATE TABLE IF NOT EXISTS assignments
                                     (id INTEGER PRIMARY KEY,
                                     assignment_type TEXT,
                                     assignment_name TEXT,
                                     assignment_grade TEXT)''')
        assignments_cursor.execute('''INSERT INTO assignments (assignment_type, assignment_name, assignment_grade)
                                     VALUES (?, ?, ?)''',
                                     (assignment_data['weight_type'], assignment_data['assignment_name'], assignment_data['grade_value']))
        assignments_db.commit()
        assignments_db.close()

        popup.destroy()

    submit_button = tk.Button(popup, text="Submit", command=submit_assignment)
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def view_assignments(course):
    assignments_window = tk.Toplevel()
    assignments_window.title(f"Assignments for {course['course_name']}")

    assignments_tree = ttk.Treeview(assignments_window, columns=("Type", "Assignment Name", "Grade"), show="headings")
    assignments_tree.heading("Type", text="Type")
    assignments_tree.heading("Assignment Name", text="Assignment Name")
    assignments_tree.heading("Grade", text="Grade")
    assignments_tree.pack(fill=tk.BOTH, expand=True)

    assignments_db = sqlite3.connect(os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db"))
    assignments_cursor = assignments_db.cursor()
    assignments_cursor.execute('''SELECT * FROM assignments''')
    assignments = assignments_cursor.fetchall()
    for assignment in assignments:
        assignments_tree.insert("", "end", values=(assignment[1], assignment[2], assignment[3]))

    assignments_db.close()

    edit_button = tk.Button(assignments_window, text="Edit", command=lambda: edit_assignment(course, assignments_tree))
    edit_button.pack()

    delete_button = tk.Button(assignments_window, text="Delete", command=lambda: delete_assignment(course, assignments_tree))
    delete_button.pack()

    back_button = tk.Button(assignments_window, text="Back", command=assignments_window.destroy)
    back_button.pack()

def edit_assignment(course, assignments_tree):
    selected_item = assignments_tree.selection()[0]
    assignment_name = assignments_tree.item(selected_item)['values'][1]
    assignment_grade = assignments_tree.item(selected_item)['values'][2]

    popup = tk.Toplevel()
    popup.title("Edit Assignment")

    assignment_name_label = tk.Label(popup, text="Assignment Name:")
    assignment_name_label.grid(row=0, column=0, padx=10, pady=5)
    assignment_name_entry = tk.Entry(popup)
    assignment_name_entry.insert(0, assignment_name)
    assignment_name_entry.grid(row=0, column=1, padx=10, pady=5)

    grade_value_label = tk.Label(popup, text="Grade Value:")
    grade_value_label.grid(row=1, column=0, padx=10, pady=5)
    grade_value_entry = tk.Entry(popup)
    grade_value_entry.insert(0, assignment_grade)
    grade_value_entry.grid(row=1, column=1, padx=10, pady=5)

    def submit_edit():
        new_assignment_name = assignment_name_entry.get()
        new_assignment_grade = grade_value_entry.get()

        assignments_db = sqlite3.connect(os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db"))
        assignments_cursor = assignments_db.cursor()
        assignments_cursor.execute('''UPDATE assignments
                                     SET assignment_name = ?,
                                         assignment_grade = ?
                                     WHERE assignment_name = ?''',
                                     (new_assignment_name, new_assignment_grade, assignment_name))
        assignments_db.commit()
        assignments_db.close()

        popup.destroy()
        view_assignments(course)

    submit_button = tk.Button(popup, text="Submit", command=submit_edit)
    submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def delete_assignment(course, assignments_tree):
    selected_items = assignments_tree.selection()
    if not selected_items:
        messagebox.showerror("Error", "Please select an assignment to delete.")
        return

    confirm_delete = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected assignment?")
    if not confirm_delete:
        return

    for item in selected_items:
        assignment_name = assignments_tree.item(item)['values'][1]

        assignments_db = sqlite3.connect(os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db"))
        assignments_cursor = assignments_db.cursor()
        assignments_cursor.execute('''DELETE FROM assignments WHERE assignment_name = ?''', (assignment_name,))
        assignments_db.commit()
        assignments_db.close()

        assignments_tree.delete(item)

def calculate_grade(course):
    exact_grade = calculate_exact_grade(course['course_name'])
    messagebox.showinfo("Exact Grade", f"The exact grade for {course['course_name']} is {exact_grade:.2f}")


root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("500x500")

update_main_menu()

button = tk.Button(root, text="Add Course", command=on_button_click)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
