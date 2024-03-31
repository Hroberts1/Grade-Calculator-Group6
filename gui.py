import tkinter as tk
import os

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
        update_main_menu() #new course button

        #write to txt file
        filename = f"{course_data['course_name'].replace(' ', '_')}_data.txt"
        with open(filename, "w") as file:
            file.write("Course Name: " + course_data['course_name'] + "\n")
            file.write("Exam Weight: " + course_data['exam_weight'] + "\n")
            file.write("Project Weight: " + course_data['project_weight'] + "\n")
            file.write("Quiz Weight: " + course_data['quiz_weight'] + "\n")
            file.write("Homework Weight: " + course_data['homework_weight'] + "\n")
            file.write("Assignment Weight: " + course_data['assignment_weight'] + "\n\n")

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

    edit_assignment_button = tk.Button(course_menu_window, text="Edit/Remove Assignment", command=lambda: edit_assignment(course))
    edit_assignment_button.pack()

    get_grade_button = tk.Button(course_menu_window, text="Get Desired Grade", command=lambda: get_desired_grade(course))
    get_grade_button.pack()

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
        # Write assignment data to the course's text file
        with open(f"{course['course_name'].replace(' ', '_')}_data.txt", "a") as file:
            file.write("Assignment Name: " + assignment_data['assignment_name'] + "\n")
            file.write("Grade Value: " + assignment_data['grade_value'] + "\n")
            file.write("Weight Type: " + assignment_data['weight_type'] + "\n\n")
        popup.destroy()

    # Create and place the submit button
    submit_button = tk.Button(popup, text="Submit", command=submit_assignment)
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create and place the back button
    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def read_course_files():
    # Read each course file and display its contents
    for filename in os.listdir():
        if filename.endswith("_data.txt"):
            course_name = filename.replace('_data.txt', '').replace('_', ' ')
            courses.append({"course_name": course_name})

# Placeholder functions for menu actions
def view_assignments(course):
    pass

def edit_assignment(course):
    pass

def get_desired_grade(course):
    pass

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
