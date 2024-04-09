import tkinter as tk

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
        with open("course_data.txt","a") as file:
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
    add_assignment_button = tk.Button(course_menu_window, text="Add Assignment", command=lambda: add_assignment(course))
    add_assignment_button.pack()

    view_assignments_button = tk.Button(course_menu_window, text="View Assignments", command=lambda: view_assignments(course))
    view_assignments_button.pack()

    edit_assignment_button = tk.Button(course_menu_window, text="Edit/Remove Assignment", command=lambda: edit_assignment(course))
    edit_assignment_button.pack()

    get_grade_button = tk.Button(course_menu_window, text="Get Desired Grade", command=lambda: get_desired_grade(course))
    get_grade_button.pack()

# You can define functions for the menu actions here
def add_assignment(course):
    print("Adding assignment for course:", course)

def view_assignments(course):
    print("Viewing assignments for course:", course)

def edit_assignment(course):
    print("Editing/Removing assignment for course:", course)

def get_desired_grade(course):
    print("Getting desired grade for course:", course)

# Create the main application window
root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("750x750")

button = tk.Button(root, text="Add Course", command=on_button_click, width=10, height=2)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
