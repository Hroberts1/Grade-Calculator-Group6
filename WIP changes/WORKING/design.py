# File: design.py
# Purpose: This script contains the design and implementation of the graphical user interface (GUI)
# for a grade calculation application. It includes classes for various popups and windows
# used in the application, such as adding courses, viewing course details, adding assignments,
# viewing assignments, editing assignments, and displaying course information.
# The GUI elements are built using Tkinter library, and the data management utilizes SQLite database.
import tkinter as tk
import os
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from calculating import calculate_course_grade

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("750x750")
        self.configure(background="#50C878")  # Emerald green color

        self.add_course_button = tk.Button(self, text="Add Course", command=self.open_add_course_popup, bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.add_course_button.pack(pady=10)

        # Display existing courses
        self.display_existing_courses()

    def open_add_course_popup(self):
        popup = AddCoursePopup(self)
        popup.on_submit(self.refresh_courses)

    def display_existing_courses(self):
        # Get existing course directories
        course_directories = [name for name in os.listdir("COURSE_BACKBONE") if os.path.isdir(os.path.join("COURSE_BACKBONE", name))]

        # Create button for each course
        for course_name in course_directories:
            course_button = tk.Button(self, text=course_name, command=lambda name=course_name: self.open_course_details(name), bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
            course_button.pack(pady=5)

    def refresh_courses(self):
        # Destroy existing course buttons
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget["text"] != "Add Course":
                widget.destroy()

        # Display existing courses
        self.display_existing_courses()

    def open_course_details(self, course_name):
        popup = CourseDetailsPopup(self, course_name)
        popup.show()

class AddCoursePopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Add Course")
        self.geometry("500x300")

        self.configure(background="#50C878")  # Emerald green color

        self.course_name_label = tk.Label(self, text="Course Name:", bg="#50C878", fg="white", font=("Arial", 12))
        self.course_name_label.grid(row=0, column=0, sticky="w")
        self.course_name_entry = tk.Entry(self, font=("Arial", 12))
        self.course_name_entry.grid(row=0, column=1)

        self.exam_weight_label = tk.Label(self, text="Exam Weight (Ex: 40%):", bg="#50C878", fg="white", font=("Arial", 12))
        self.exam_weight_label.grid(row=1, column=0, sticky="w")
        self.exam_weight_entry = tk.Entry(self, font=("Arial", 12))
        self.exam_weight_entry.grid(row=1, column=1)

        self.project_weight_label = tk.Label(self, text="Project Weight (Ex: 20%):", bg="#50C878", fg="white", font=("Arial", 12))
        self.project_weight_label.grid(row=2, column=0, sticky="w")
        self.project_weight_entry = tk.Entry(self, font=("Arial", 12))
        self.project_weight_entry.grid(row=2, column=1)

        self.homework_weight_label = tk.Label(self, text="Homework Weight (Ex: 10%):", bg="#50C878", fg="white", font=("Arial", 12))
        self.homework_weight_label.grid(row=3, column=0, sticky="w")
        self.homework_weight_entry = tk.Entry(self, font=("Arial", 12))
        self.homework_weight_entry.grid(row=3, column=1)

        self.quiz_weight_label = tk.Label(self, text="Quiz Weight (Ex: 10%):", bg="#50C878", fg="white", font=("Arial", 12))
        self.quiz_weight_label.grid(row=4, column=0, sticky="w")
        self.quiz_weight_entry = tk.Entry(self, font=("Arial", 12))
        self.quiz_weight_entry.grid(row=4, column=1)

        self.assignment_weight_label = tk.Label(self, text="Assignment Weight (Ex: 10%):", bg="#50C878", fg="white", font=("Arial", 12))
        self.assignment_weight_label.grid(row=5, column=0, sticky="w")
        self.assignment_weight_entry = tk.Entry(self, font=("Arial", 12))
        self.assignment_weight_entry.grid(row=5, column=1)

        self.back_button = tk.Button(self, text="Back", command=self.destroy, fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.back_button.grid(row=6, column=0, pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data, fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.submit_button.grid(row=6, column=1, pady=10)

    def submit_data(self):
        course_name = self.course_name_entry.get()
        exam_weight = self.exam_weight_entry.get()
        project_weight = self.project_weight_entry.get()
        homework_weight = self.homework_weight_entry.get()
        quiz_weight = self.quiz_weight_entry.get()
        assignment_weight = self.assignment_weight_entry.get()

        if not (course_name and exam_weight and project_weight and homework_weight and quiz_weight and assignment_weight):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create subdirectory for the course
        course_directory = os.path.join("COURSE_BACKBONE", course_name)
        if not os.path.exists(course_directory):
            os.makedirs(course_directory)
            messagebox.showinfo("Success", f"Course '{course_name}' added successfully.")
        else:
            messagebox.showerror("Error", f"Course '{course_name}' already exists.")

        # Create SQLite database
        db_name = os.path.join(course_directory, f"{course_name}_info.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS course_info
                     (course_name TEXT, exam_weight INT, project_weight INT, homework_weight INT,
                     quiz_weight INT, assignment_weight INT)''')

        # Insert data into table
        c.execute('''INSERT INTO course_info VALUES (?, ?, ?, ?, ?, ?)''',
                  (course_name, exam_weight, project_weight, homework_weight, quiz_weight, assignment_weight))

        conn.commit()
        conn.close()

        # Close the popup window
        self.destroy()

    def on_submit(self, callback):
        self.callback = callback

        def submit_and_refresh():
            self.submit_data()
            self.callback()

        self.submit_button.config(command=submit_and_refresh)

class CourseDetailsPopup(tk.Toplevel):
    def __init__(self, master, course_name):
        super().__init__(master)
        self.title(f"{course_name} Details")
        self.geometry("450x500")

        self.course_name = course_name

        self.view_info_button = tk.Button(self, text="View Course Information", command=self.view_course_info, bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.view_info_button.pack(pady=10)

        self.add_assignment_button = tk.Button(self, text="Add Assignment", command=self.add_assignment_popup, bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.add_assignment_button.pack(pady=10)

        self.view_assignments_button = tk.Button(self, text="View Assignments", command=self.view_assignments_popup, bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.view_assignments_button.pack(pady=10)

        self.calculate_grade_button = tk.Button(self, text="Calculate Grade", command=self.calculate_grade, bg="white", fg="#000000", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="black", highlightthickness=1)
        self.calculate_grade_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.destroy, bg="#6495ED", fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
        self.back_button.pack(pady=10)

    def view_course_info(self):
        db_name = os.path.join("COURSE_BACKBONE", f"{self.course_name}", f"{self.course_name}_info.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Fetch course information
        c.execute("SELECT * FROM course_info")
        course_info = c.fetchone()  # Assuming only one row for simplicity

        conn.close()

        if course_info:
            # Create a new popup window to display course information
            info_popup = CourseInfoPopup(self, course_info)
            info_popup.show()
        else:
            messagebox.showerror("Error", "No course information found.")

    def add_assignment_popup(self):
        popup = AddAssignmentPopup(self, self.course_name)
        popup.show()

    def view_assignments_popup(self):
        popup = AssignmentsPopup(self, self.course_name)
        popup.show()

    def calculate_grade(self):
        db_name = os.path.join("COURSE_BACKBONE", f"{self.course_name}", f"{self.course_name}_assignments.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Fetch all assignment grades
        c.execute("SELECT assignment_grade FROM assignments")
        assignment_grades = c.fetchall()

        conn.close()

        # Calculate the course grade
        course_grade = calculate_course_grade(assignment_grades)

        # Display the course grade
        messagebox.showinfo("Course Grade", f"The calculated grade for {self.course_name} is {course_grade}%.")

    def show(self):
        self.grab_set()
        self.wait_window()

class AddAssignmentPopup(tk.Toplevel):
    def __init__(self, master, course_name):
        super().__init__(master)
        self.title("Add Assignment")
        self.geometry("400x200")

        self.course_name = course_name

        self.assignment_name_label = tk.Label(self, text="Assignment Name:", fg="black", font=("Arial", 12))
        self.assignment_name_label.grid(row=0, column=0, sticky="w")
        self.assignment_name_entry = tk.Entry(self, font=("Arial", 12))
        self.assignment_name_entry.grid(row=0, column=1)

        self.assignment_type_label = tk.Label(self, text="Assignment Type:", fg="black", font=("Arial", 12))
        self.assignment_type_label.grid(row=1, column=0, sticky="w")
        self.assignment_type_var = tk.StringVar(self)
        self.assignment_type_var.set("Homework")  # Default assignment type
        self.assignment_type_dropdown = tk.OptionMenu(self, self.assignment_type_var, "Homework", "Quiz", "Project", "Exam", "Other")
        self.assignment_type_dropdown.config(font=("Arial", 12), fg="#000000", borderwidth=1, relief="solid")
        self.assignment_type_dropdown.grid(row=1, column=1)

        self.assignment_grade_label = tk.Label(self, text="Assignment Grade:", fg="black", font=("Arial", 12))
        self.assignment_grade_label.grid(row=2, column=0, sticky="w")
        self.assignment_grade_entry = tk.Entry(self, font=("Arial", 12))
        self.assignment_grade_entry.grid(row=2, column=1)

        self.back_button = tk.Button(self, text="Back", command=self.destroy, bg="#6495ED", fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
        self.back_button.grid(row=3, column=0, pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data, bg="#6495ED", fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
        self.submit_button.grid(row=3, column=1, pady=10)

    def submit_data(self):
        assignment_name = self.assignment_name_entry.get()
        assignment_type = self.assignment_type_var.get()
        assignment_grade = self.assignment_grade_entry.get()

        if not (assignment_name and assignment_grade):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create SQLite database for assignments
        db_name = os.path.join("COURSE_BACKBONE", self.course_name, f"{self.course_name}_assignments.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Create table if not exists
        c.execute('''CREATE TABLE IF NOT EXISTS assignments
                     (assignment_name TEXT, assignment_type TEXT, assignment_grade REAL)''')

        # Insert data into table
        c.execute('''INSERT INTO assignments VALUES (?, ?, ?)''',
                  (assignment_name, assignment_type, assignment_grade))

        conn.commit()
        conn.close()

        # Close the popup window
        self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()

class AssignmentsPopup(tk.Toplevel):
    def __init__(self, master, course_name):
        super().__init__(master)
        self.title(f"{course_name} Assignments")
        self.geometry("600x500")

        self.course_name = course_name

        # Disable automatic resizing of the window
        self.pack_propagate(False)

        # Create a table to display course assignments
        self.tree = ttk.Treeview(self, columns=("Assignment Name", "Assignment Type", "Assignment Grade"), show="headings")
        self.tree.heading("Assignment Name", text="Assignment Name")
        self.tree.heading("Assignment Type", text="Assignment Type")
        self.tree.heading("Assignment Grade", text="Assignment Grade")
        self.tree.pack(fill="both", expand=True)  # Fill both x and y directions

        # Load assignments from database
        self.load_assignments()

        # Buttons
        button_width = 20
        button_height = 3

        self.back_button = tk.Button(self, text="Back", command=self.destroy, width=button_width, height=button_height)
        self.back_button.pack(side="left", padx=10, pady=10, expand=True)

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_assignment, width=button_width, height=button_height)
        self.edit_button.pack(side="left", padx=10, pady=10, expand=True)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_assignment, width=button_width, height=button_height)
        self.delete_button.pack(side="left", padx=10, pady=10, expand=True)

    def load_assignments(self):
        db_name = os.path.join("COURSE_BACKBONE", self.course_name, f"{self.course_name}_assignments.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("SELECT * FROM assignments")
        assignments = c.fetchall()

        for assignment in assignments:
            self.tree.insert("", "end", values=assignment)

        conn.close()

    def edit_assignment(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an assignment to edit.")
            return

        assignment_name = self.tree.item(selected_item, "values")[0]
        assignment_type = self.tree.item(selected_item, "values")[1]
        assignment_grade = self.tree.item(selected_item, "values")[2]

        popup = EditAssignmentPopup(self, self.course_name, assignment_name, assignment_type, assignment_grade)
        popup.show()

    def delete_assignment(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an assignment to delete.")
            return

        confirmation = messagebox.askyesno("Delete Assignment", "Are you sure you want to delete this assignment?")
        if confirmation:
            assignment_name = self.tree.item(selected_item, "values")[0]

            db_name = os.path.join("COURSE_BACKBONE", self.course_name, f"{self.course_name}_assignments.db")
            conn = sqlite3.connect(db_name)
            c = conn.cursor()

            c.execute("DELETE FROM assignments WHERE assignment_name=?", (assignment_name,))
            conn.commit()
            conn.close()

            self.tree.delete(selected_item)

            messagebox.showinfo("Success", "Assignment deleted successfully.")

class EditAssignmentPopup(tk.Toplevel):
    def __init__(self, master, course_name, assignment_name, assignment_type, assignment_grade):
        super().__init__(master)
        self.title("Edit Assignment")
        self.geometry("400x200")

        self.course_name = course_name
        self.assignment_name = assignment_name

        self.assignment_name_label = tk.Label(self, text="Assignment Name:", fg="black", font=("Arial", 12))
        self.assignment_name_label.grid(row=0, column=0, sticky="w")
        self.assignment_name_entry = tk.Entry(self, font=("Arial", 12))
        self.assignment_name_entry.insert(0, assignment_name)
        self.assignment_name_entry.grid(row=0, column=1)

        self.assignment_type_label = tk.Label(self, text="Assignment Type:", fg="black", font=("Arial", 12))
        self.assignment_type_label.grid(row=1, column=0, sticky="w")
        self.assignment_type_var = tk.StringVar(self)
        self.assignment_type_var.set(assignment_type)
        self.assignment_type_dropdown = tk.OptionMenu(self, self.assignment_type_var, "Homework", "Quiz", "Project", "Exam", "Other")
        self.assignment_type_dropdown.config(font=("Arial", 12), fg="#000000", borderwidth=1, relief="solid")
        self.assignment_type_dropdown.grid(row=1, column=1)

        self.assignment_grade_label = tk.Label(self, text="Assignment Grade:", fg="black", font=("Arial", 12))
        self.assignment_grade_label.grid(row=2, column=0, sticky="w")
        self.assignment_grade_entry = tk.Entry(self, font=("Arial", 12))
        self.assignment_grade_entry.insert(0, assignment_grade)
        self.assignment_grade_entry.grid(row=2, column=1)

        self.back_button = tk.Button(self, text="Back", command=self.destroy, fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
        self.back_button.grid(row=3, column=0, pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data, fg="black", font=("Arial", 12), padx=10, pady=5, borderwidth=1, relief="solid", highlightbackground="white", highlightthickness=1)
        self.submit_button.grid(row=3, column=1, pady=10)

    def submit_data(self):
        new_assignment_name = self.assignment_name_entry.get()
        new_assignment_type = self.assignment_type_var.get()
        new_assignment_grade = self.assignment_grade_entry.get()

        if not (new_assignment_name and new_assignment_grade):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        db_name = os.path.join("COURSE_BACKBONE", self.course_name, f"{self.course_name}_assignments.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("UPDATE assignments SET assignment_name=?, assignment_type=?, assignment_grade=? WHERE assignment_name=?",
                  (new_assignment_name, new_assignment_type, new_assignment_grade, self.assignment_name))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Assignment updated successfully.")

        self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()

class CourseInfoPopup(tk.Toplevel):
    def __init__(self, master, course_info):
        super().__init__(master)
        self.title("Course Information")
        self.geometry("400x200")

        self.course_info = course_info

        # Create a table to display course information
        self.tree = ttk.Treeview(self, columns=("Weight Type", "Weight Value"), show="headings")
        self.tree.heading("Weight Type", text="Weight Type")
        self.tree.heading("Weight Value", text="Weight Value")
        self.tree.pack(fill="both", expand=True)  # Fill both x and y directions

        # Insert course information into the table
        self.tree.insert("", "end", values=("Exam Weight", course_info[1]))
        self.tree.insert("", "end", values=("Project Weight", course_info[2]))
        self.tree.insert("", "end", values=("Homework Weight", course_info[3]))
        self.tree.insert("", "end", values=("Quiz Weight", course_info[4]))
        self.tree.insert("", "end", values=("Assignment Weight", course_info[5]))

        # Button to close the popup window
        self.close_button = tk.Button(self, text="Close", command=self.destroy, width=20, height=2)
        self.close_button.pack(pady=10)

    def calculate_grade_popup(self):
        db_name = os.path.join("COURSE_BACKBONE", self.course_name, f"{self.course_name}_assignments.db")
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        # Fetch assignment grades
        c.execute("SELECT assignment_grade FROM assignments")
        grades = c.fetchall()

        conn.close()

        total_grade = sum(float(grade[0]) for grade in grades) if grades else 0
        total_assignments = len(grades)

        if total_assignments > 0:
            average_grade = total_grade / total_assignments
            grade_message = f"Total Assignments: {total_assignments}\nTotal Grade: {total_grade}\nAverage Grade: {average_grade:.2f}"
            messagebox.showinfo("Grade Summary", grade_message)
        else:
            messagebox.showinfo("Grade Summary", "No assignments found for this course.")
    

    def show(self):
        self.grab_set()
        self.wait_window()


def main():
    app = MainMenu()
    app.mainloop()

if __name__ == "__main__":
    main()
