import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os
import sqlite3
from calculations import calculate_exact_grade

courses = []
MAIN_DIRECTORY = "COURSES"

def fetch_courses_from_db():
    for root, dirs, files in os.walk(MAIN_DIRECTORY):
        for filename in files:
            if filename.endswith("_info.db"):
                course_name = filename.replace('_info.db', '').replace('_', ' ')
                courses.append({"course_name": course_name})

fetch_courses_from_db()

def calculate_letter_grade(exact_grade):
    if 90 <= exact_grade <= 100:
        return "A"
    elif 80 <= exact_grade < 90:
        return "B"
    elif 70 <= exact_grade < 80:
        return "C"
    elif 60 <= exact_grade < 70:
        return "D"
    else:
        return "F"

def on_button_click():
    create_add_course_popup()

def create_add_course_popup():
    popup = tk.Toplevel()
    popup.title("Add Course")

    # Function to validate integer input
    def validate_integer(input_str):
        if input_str == "":
            return True  # Allow empty string
        try:
            int(input_str)
            return True
        except ValueError:
            return False

    # Function to validate non-empty input
    def validate_non_empty(input_str):
        return len(input_str.strip()) > 0

    # Validate and accept only integers for grade weights
    validate_int_cmd = popup.register(validate_integer)
    validate_non_empty_cmd = popup.register(validate_non_empty)

    course_name_label = tk.Label(popup, text="Course Name:")
    course_name_label.grid(row=0, column=0, padx=10, pady=5)
    course_name_entry = tk.Entry(popup, validate="key", validatecommand=(validate_non_empty_cmd, '%P'))
    course_name_entry.grid(row=0, column=1, padx=10, pady=5)

    # Add a label to indicate the name is required
    course_name_required_label = tk.Label(popup, text="(Required)", fg="red")
    course_name_required_label.grid(row=0, column=2, padx=5, pady=5)

    exam_weight_label = tk.Label(popup, text="Exam Weight (Ex: 40%):")
    exam_weight_label.grid(row=1, column=0, padx=10, pady=5)
    exam_weight_entry = tk.Entry(popup, validate="key", validatecommand=(validate_int_cmd, '%P'))
    exam_weight_entry.grid(row=1, column=1, padx=10, pady=5)

    # Add a label to indicate the weight is required
    exam_weight_required_label = tk.Label(popup, text="(Required)", fg="red")
    exam_weight_required_label.grid(row=1, column=2, padx=5, pady=5)

    project_weight_label = tk.Label(popup, text="Project Weight (Ex: 20%):")
    project_weight_label.grid(row=2, column=0, padx=10, pady=5)
    project_weight_entry = tk.Entry(popup, validate="key", validatecommand=(validate_int_cmd, '%P'))
    project_weight_entry.grid(row=2, column=1, padx=10, pady=5)

    # Add a label to indicate the weight is required
    project_weight_required_label = tk.Label(popup, text="(Required)", fg="red")
    project_weight_required_label.grid(row=2, column=2, padx=5, pady=5)

    quiz_weight_label = tk.Label(popup, text="Quiz Weight (Ex: 10%):")
    quiz_weight_label.grid(row=3, column=0, padx=10, pady=5)
    quiz_weight_entry = tk.Entry(popup, validate="key", validatecommand=(validate_int_cmd, '%P'))
    quiz_weight_entry.grid(row=3, column=1, padx=10, pady=5)

    # Add a label to indicate the weight is required
    quiz_weight_required_label = tk.Label(popup, text="(Required)", fg="red")
    quiz_weight_required_label.grid(row=3, column=2, padx=5, pady=5)

    homework_weight_label = tk.Label(popup, text="Homework Weight (Ex: 15%):")
    homework_weight_label.grid(row=4, column=0, padx=10, pady=5)
    homework_weight_entry = tk.Entry(popup, validate="key", validatecommand=(validate_int_cmd, '%P'))
    homework_weight_entry.grid(row=4, column=1, padx=10, pady=5)

    # Add a label to indicate the weight is required
    homework_weight_required_label = tk.Label(popup, text="(Required)", fg="red")
    homework_weight_required_label.grid(row=4, column=2, padx=5, pady=5)

    assignment_weight_label = tk.Label(popup, text="Assignment Weight (Ex: 15%):")
    assignment_weight_label.grid(row=5, column=0, padx=10, pady=5)
    assignment_weight_entry = tk.Entry(popup, validate="key", validatecommand=(validate_int_cmd, '%P'))
    assignment_weight_entry.grid(row=5, column=1, padx=10, pady=5)

    # Add a label to indicate the weight is required
    assignment_weight_required_label = tk.Label(popup, text="(Required)", fg="red")
    assignment_weight_required_label.grid(row=5, column=2, padx=5, pady=5)

    def submit_course():
        # Check if all grade weight fields are filled
        if not all([
            validate_non_empty(course_name_entry.get()),
            validate_non_empty(exam_weight_entry.get()),
            validate_non_empty(project_weight_entry.get()),
            validate_non_empty(quiz_weight_entry.get()),
            validate_non_empty(homework_weight_entry.get()),
            validate_non_empty(assignment_weight_entry.get())
        ]):
            messagebox.showerror("Error", "Please fill out all required fields.")
            return
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

    submit_button = ttk.Button(popup, text="Submit", command=submit_course, style='TButton')
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    back_button = ttk.Button(popup, text="Back", command=popup.destroy, style='TButton')
    back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def update_main_menu():
    root = tk.Tk()
    root.title("Grade Calculator Application")
    root.geometry("500x500")
    root.configure(bg='#009E60')

    style = ttk.Style()
    style.configure('TButton', relief=tk.RAISED, borderwidth=.75, foreground='black', background='black', font=('Arial', 13), anchor='center', borderradius=10)
    style.map('TButton', background=[('active', '!disabled', 'black')], bordercolor=[('active', 'black')])

    # Clear previous main menu
    for widget in root.winfo_children():
        widget.destroy()

    # Calculate center position
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))

    # Add course buttons
    for i, course in enumerate(courses):
        course_button = ttk.Button(root, text=course["course_name"], command=lambda c=course: on_course_button_click(root, c), style='TButton')
        course_button.pack(pady=5)

    button = ttk.Button(root, text="Add Course", command=on_button_click, style='TButton')
    button.pack(pady=10)

    root.mainloop()

def on_course_button_click(root, course):
    course_menu_window = tk.Toplevel(root)
    course_menu_window.title(f"Menu for {course['course_name']}")

    view_course_info_button = ttk.Button(course_menu_window, text="View Course Info", command=lambda: view_course_info(course), style='TButton')
    view_course_info_button.pack()

    add_assignment_button = ttk.Button(course_menu_window, text="Add Assignment", command=lambda: create_add_assignment_popup(course), style='TButton')
    add_assignment_button.pack()

    view_assignments_button = ttk.Button(course_menu_window, text="View Assignments", command=lambda: view_assignments(course), style='TButton')
    view_assignments_button.pack()

    calculate_grade_button = ttk.Button(course_menu_window, text="Calculate Grade", command=lambda: calculate_grade(course), style='TButton')
    calculate_grade_button.pack()

def view_course_info(course):
    course_info_window = tk.Toplevel()
    course_info_window.title(f"Course Information for {course['course_name']}")

    course_info_tree = ttk.Treeview(course_info_window, columns=("Property", "Value"), show="headings")
    course_info_tree.heading("Property", text="Property")
    course_info_tree.heading("Value", text="Value")
    course_info_tree.pack(fill=tk.BOTH, expand=True)

    course_info_db_path = os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_info.db")
    with sqlite3.connect(course_info_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM course_info''')
        course_info = cursor.fetchone()
        course_info_tree.insert("", "end", values=("Exam Weight", course_info[2]))
        course_info_tree.insert("", "end", values=("Project Weight", course_info[3]))
        course_info_tree.insert("", "end", values=("Quiz Weight", course_info[4]))
        course_info_tree.insert("", "end", values=("Homework Weight", course_info[5]))
        course_info_tree.insert("", "end", values=("Assignment Weight", course_info[6]))

    back_button = ttk.Button(course_info_window, text="Back", command=course_info_window.destroy, style='TButton')
    back_button.pack()

def create_add_assignment_popup(course):
    popup = tk.Toplevel()
    popup.title("Add Assignment")

    # Function to validate integer or decimal input
    def validate_number(input_str):
        if input_str == "":
            return True  # Allow empty string
        try:
            float(input_str)
            return True
        except ValueError:
            return False

    # Validate and accept integers or decimals for grade values
    validate_number_cmd = popup.register(validate_number)

    assignment_name_label = tk.Label(popup, text="Assignment Name:")
    assignment_name_label.grid(row=0, column=0, padx=10, pady=5)
    assignment_name_entry = tk.Entry(popup)
    assignment_name_entry.grid(row=0, column=1, padx=10, pady=5)

    grade_value_label = tk.Label(popup, text="Grade Value:")
    grade_value_label.grid(row=1, column=0, padx=10, pady=5)
    grade_value_entry = tk.Entry(popup, validate="key", validatecommand=(validate_number_cmd, '%P'))
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

    submit_button = ttk.Button(popup, text="Submit", command=submit_assignment, style='TButton')
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    back_button = ttk.Button(popup, text="Back", command=popup.destroy, style='TButton')
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def view_assignments(course):
    assignments_window = tk.Toplevel()
    assignments_window.title(f"Assignments for {course['course_name']}")

    assignments_tree = ttk.Treeview(assignments_window, columns=("Name", "Grade"), show="headings")
    assignments_tree.heading("Name", text="Name")
    assignments_tree.heading("Grade", text="Grade")
    assignments_tree.pack(fill=tk.BOTH, expand=True)

    assignments_db_path = os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db")
    with sqlite3.connect(assignments_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM assignments''')
        assignments = cursor.fetchall()
        for assignment in assignments:
            assignments_tree.insert("", "end", values=(assignment[2], assignment[3]))

    back_button = ttk.Button(assignments_window, text="Back", command=assignments_window.destroy, style='TButton')
    back_button.pack()

def calculate_grade(course):
    course_directory = os.path.join(MAIN_DIRECTORY, course['course_name'].replace(' ', '_'))
    course_info_db_path = os.path.join(course_directory, f"{course['course_name'].replace(' ', '_')}_info.db")
    course_assignments_db_path = os.path.join(course_directory, f"{course['course_name'].replace(' ', '_')}_assignments.db")

    if not os.path.exists(course_info_db_path):
        messagebox.showerror("Error", "No course information found.")
        return

    if not os.path.exists(course_assignments_db_path):
        messagebox.showerror("Error", "No assignments found.")
        return

    with sqlite3.connect(course_info_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM course_info''')
        course_info = cursor.fetchone()

    with sqlite3.connect(course_assignments_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM assignments''')
        assignments = cursor.fetchall()

    total_grade = 0
    total_weight = 0

    for assignment in assignments:
        total_weight += float(course_info[2 + ['Exam', 'Project', 'Quiz', 'Homework', 'Assignment'].index(assignment[1])])
        total_grade += float(assignment[2]) * float(course_info[2 + ['Exam', 'Project', 'Quiz', 'Homework', 'Assignment'].index(assignment[1])]) / 100

    exact_grade = calculate_exact_grade(total_grade, total_weight)
    letter_grade = calculate_letter_grade(exact_grade)

    messagebox.showinfo("Grade", f"Exact Grade: {exact_grade}\nLetter Grade: {letter_grade}")

update_main_menu()
