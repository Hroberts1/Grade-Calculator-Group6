import tkinter as tk
import json

# Create the main application window
# root = tk.Tk()
# root.title("Grade Calculator Application")
# root.geometry("750x750")


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


        # Create buttons for each course in the list
    for i, course in enumerate(courses):
        # Create a frame to hold the course button and its menu
        frame = tk.Frame(root)
        frame.grid(row=i+1, column=0, padx=10, pady=5)

        # Create the course button
        course_button = tk.Button(frame, text=course["course_name"], command=lambda c=course: on_course_button_click(c))
        course_button.grid(row=0, column=0)

        # Create the menu for the course button
        course_menu = tk.Menu(frame, tearoff=0)
        course_menu.add_command(label="View Course", command=lambda c=course: view_course(c))
        course_menu.add_command(label="Add Assignment", command=lambda c=course: add_assignment(c))
        course_menu.add_command(label="Delete Assignment", command=lambda c=course: delete_assignment(c))
        course_menu.add_separator()
        course_menu.add_command(label="Delete Course", command=lambda c=course: delete_course(c))
        course_menu.add_command(label="Back", command=lambda c=course: back())
        
        # Attach the menu to the course button
        course_button.bind("<Button-3>", lambda event, menu=course_menu: menu.post(event.x_root, event.y_root))

def view_course(course):
    print("View course:", course)

def add_assignment(course):
    print("Add assignment:", course)

def delete_assignment(course):
    print("Delete assignment:", course)

def delete_course(course):
    print("Delete course:", course)

def back():
    print("Back")

# Create the main application window
root = tk.Tk()
root.title("Grade Clalculator")

# Set the window size to 750x750 pixels
root.geometry("750x750")

# Create a button widget with a square shape
button = tk.Button(root, text="Add Course", command=on_button_click, width=10, height=2)
button.grid(row=0, column=0, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()

def on_course_button_click(course):
    # This function will be called when a course button is clicked
    print("Course button clicked:", course)

# Create the main application window
root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("750x750")

# Create a button widget with a square shape
button = tk.Button(root, text="Add Course", command=on_button_click, width=10, height=2)
button.grid(row=0, column=0, padx=10, pady=5)




# Run the Tkinter event loop
root.mainloop()
