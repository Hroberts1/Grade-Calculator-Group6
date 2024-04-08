import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os
import sqlite3

courses = []

def on_button_click():
    # This function will be called when the "Add Course" button is clicked
    # Create and display the pop-up window for adding a course
    create_add_course_popup()

def create_add_course_popup():
    # Create the pop-up window
    popup = tk.Toplevel()
    popup.title("Add Course")

    # Create labels and entry widgets for course name and weights
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

    # Function to handle the submit button click
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

        # Create directory for course and database for assignments
        create_course_directory(course_data['course_name'])

        # Write course data to the course's database
        course_db = sqlite3.connect(os.path.join(course_data['course_name'].replace(' ', '_'), f"{course_data['course_name'].replace(' ', '_')}_info.db"))
        course_cursor = course_db.cursor()

        course_cursor.execute('''CREATE TABLE IF NOT EXISTS course_info
                                (course_name TEXT, exam_weight TEXT, project_weight TEXT,
                                quiz_weight TEXT, homework_weight TEXT, assignment_weight TEXT)''')

        course_cursor.execute('''INSERT INTO course_info
                                (course_name, exam_weight, project_weight, quiz_weight,
                                homework_weight, assignment_weight)
                                VALUES (?, ?, ?, ?, ?, ?)''',
                                (course_data['course_name'], course_data['exam_weight'], course_data['project_weight'],
                                course_data['quiz_weight'], course_data['homework_weight'], course_data['assignment_weight']))

        course_db.commit()
        course_db.close()

        popup.destroy()

    # Create and place the submit button
    submit_button = tk.Button(popup, text="Submit", command=submit_course)
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Create and place the back button
    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

def update_main_menu():
    for i, course in enumerate(courses):
        frame = tk.Frame(root)
        frame.grid(row=i+1, column=0, padx=10, pady=5)

        course_button = tk.Button(frame, text=course["course_name"], command=lambda c=course: on_course_button_click(root, c))
        course_button.grid(row=0, column=0)

def on_course_button_click(root, course):
    # This function will be called when a course button is clicked
    print("Course button clicked:", course)

    # Create a new window to display the menu options
    course_menu_window = tk.Toplevel(root)
    course_menu_window.title(f"Menu for {course['course_name']}")

    # Add menu items or any other content here
    add_assignment_button = tk.Button(course_menu_window, text="Add Assignment", command=lambda: create_add_assignment_popup(course))
    add_assignment_button.pack()

    view_assignments_button = tk.Button(course_menu_window, text="View Assignments", command=lambda: view_assignments(course))
    view_assignments_button.pack()

   # get_grade_button = tk.Button(course_menu_window, text="Get Desired Grade", command=lambda: get_desired_grade(course))
   #get_grade_button.pack()

def create_course_directory(course_name):
    # Create directory for the course if it doesn't exist
    directory_name = course_name.replace(' ', '_')
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def create_add_assignment_popup(course):
    # Create the pop-up window
    popup = tk.Toplevel()
    popup.title("Add Assignment")

    # Create labels and entry widgets for assignment details
    assignment_name_label = tk.Label(popup, text="Assignment Name:")
    assignment_name_label.grid(row=0, column=0, padx=10, pady=5)
    assignment_name_entry = tk.Entry(popup)
    assignment_name_entry.grid(row=0, column=1, padx=10, pady=5)

    grade_value_label = tk.Label(popup, text="Grade Value:")
    grade_value_label.grid(row=1, column=0, padx=10, pady=5)
    grade_value_entry = tk.Entry(popup)
    grade_value_entry.grid(row=1, column=1, padx=10, pady=5)

    # Dropdown menu for weight types
    weight_type_label = tk.Label(popup, text="Weight Type:")
    weight_type_label.grid(row=2, column=0, padx=10, pady=5)
    weight_types = ["Exam", "Project", "Quiz", "Homework", "Assignment"]
    weight_type_var = tk.StringVar()
    weight_type_var.set(weight_types[0])  # Default value
    weight_type_dropdown = tk.OptionMenu(popup, weight_type_var, *weight_types)
    weight_type_dropdown.grid(row=2, column=1, padx=10, pady=5)

    # Function to handle the submit button click
    def submit_assignment():
        assignment_data = {
            "assignment_name": assignment_name_entry.get(),
            "grade_value": grade_value_entry.get(),
            "weight_type": weight_type_var.get(),
        }
        # Write assignment data to the course's database
        assignment_db = sqlite3.connect(os.path.join(course['course_name'].replace(' ', '_'), f"{course['course_name'].replace(' ', '_')}_assignments.db"))
        assignment_cursor = assignment_db.cursor()

        assignment_cursor.execute('''CREATE TABLE IF NOT EXISTS assignments
                                    (assignment_number INTEGER PRIMARY KEY, assignment_type TEXT,
                                    assignment_name TEXT, assignment_grade TEXT)''')

        assignment_cursor.execute('''INSERT INTO assignments
                                    (assignment_type, assignment_name, assignment_grade)
                                    VALUES (?, ?, ?)''',
                                    (assignment_data['weight_type'], assignment_data['assignment_name'], assignment_data['grade_value']))

        assignment_db.commit()
        assignment_db.close()

        popup.destroy()

    # Create and place the submit button
    submit_button = tk.Button(popup, text="Submit", command=submit_assignment)
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create and place the back button
    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def view_assignments(course):
    # Create a new window to display assignments
    assignments_window = tk.Toplevel()
    assignments_window.title(f"Assignments for {course['course_name']}")

    # Create a Treeview widget to display assignments as a table
    assignments_tree = ttk.Treeview(assignments_window, columns=("Type", "Assignment Name", "Grade"), show="headings")
    assignments_tree.heading("Type", text="Type")
    assignments_tree.heading("Assignment Name", text="Assignment Name")
    assignments_tree.heading("Grade", text="Grade")
    assignments_tree.pack(fill=tk.BOTH, expand=True)

    # Retrieve assignments from the database
    course_directory = course['course_name'].replace(' ', '_')
    assignments_db_path = os.path.join(course_directory, f"{course_directory}_assignments.db")
    if os.path.exists(assignments_db_path):
        assignments_db = sqlite3.connect(assignments_db_path)
        assignments_cursor = assignments_db.cursor()

        # Fetch assignments from the database
        assignments_cursor.execute('''SELECT * FROM assignments''')
        assignments = assignments_cursor.fetchall()

        # Display assignments in the Treeview widget
        for assignment in assignments:
            assignments_tree.insert("", "end", values=(assignment[1], assignment[2], assignment[3]))

        # Close the database connection
        assignments_db.close()
    else:
        no_assignments_label = tk.Label(assignments_window, text="No assignments found.")
        no_assignments_label.pack()

    # Create buttons for Edit, Delete, and Back
    edit_button = tk.Button(assignments_window, text="Edit", command=lambda: edit_assignment(assignments_tree))
    edit_button.pack(side=tk.LEFT, padx=10, pady=10)

    delete_button = tk.Button(assignments_window, text="Delete", command=lambda: delete_assignment(assignments_tree))
    delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    back_button = tk.Button(assignments_window, text="Back", command=assignments_window.destroy)
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

def edit_assignment(assignments_tree):
    # Get the selected item from the Treeview widget
    selected_item = assignments_tree.focus()

    if selected_item:
        # Retrieve the assignment details from the selected item
        assignment_details = assignments_tree.item(selected_item, "values")
        assignment_name = assignment_details[1]
        assignment_grade = assignment_details[2]

        # Create the pop-up window for editing the assignment
        edit_popup = tk.Toplevel()
        edit_popup.title("Edit Assignment")

        # Create labels and entry widgets for assignment details
        assignment_name_label = tk.Label(edit_popup, text="Assignment Name:")
        assignment_name_label.grid(row=0, column=0, padx=10, pady=5)
        assignment_name_entry = tk.Entry(edit_popup)
        assignment_name_entry.insert(0, assignment_name)  # Populate with current assignment name
        assignment_name_entry.grid(row=0, column=1, padx=10, pady=5)

        grade_value_label = tk.Label(edit_popup, text="Grade Value:")
        grade_value_label.grid(row=1, column=0, padx=10, pady=5)
        grade_value_entry = tk.Entry(edit_popup)
        grade_value_entry.insert(0, assignment_grade)  # Populate with current assignment grade
        grade_value_entry.grid(row=1, column=1, padx=10, pady=5)

        # Function to handle the submit button click
        def submit_edit():
            new_assignment_name = assignment_name_entry.get()
            new_assignment_grade = grade_value_entry.get()

            # Update the assignment details in the Treeview widget
            assignments_tree.item(selected_item, values=(assignment_details[0], new_assignment_name, new_assignment_grade))

            # Close the pop-up window
            edit_popup.destroy()

        # Create and place the submit button
        submit_button = tk.Button(edit_popup, text="Submit", command=submit_edit)
        submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    else:
        messagebox.showerror("Error", "No assignment selected for editing.")

def delete_assignment(assignments_tree):
    # Get the selected item from the Treeview widget
    selected_item = assignments_tree.focus()

    if selected_item:
        # Delete the selected item from the Treeview widget
        assignments_tree.delete(selected_item)
    else:
        messagebox.showerror("Error", "No assignment selected for deletion.")

def read_course_files():
    # Read each course file and display its contents
    for filename in os.listdir():
        if filename.endswith("_info.db"):
            course_name = filename.replace('_info.db', '').replace('_', ' ')
            courses.append({"course_name": course_name})

# Read course files on program start
read_course_files()

# Create the main application window
root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("750x750")

# Add course buttons
update_main_menu()

# Add Course button
button = tk.Button(root, text="Add Course", command=on_button_click, width=10, height=2)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
