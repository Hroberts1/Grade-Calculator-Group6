# Python program to create a table

import tkinter as tk
from CALCULATOR import calc_needed_quiz_avg, calc_needed_exam_avg, calc_needed_assignment_avg, calc_needed_homework_avg

def run_A_Calculator(the_class):
    def on_button_click(the_class):
        # This function will be called when the "A-Calculator" button is clicked
        # Create and display the pop-up window for adding a course
        create_needed_grade_popup(the_class)


    def create_needed_grade_popup(the_class):
        # Create the pop-up window
        popup = tk.Toplevel()

        # Create labels and entry widgets for course name and weights
        '''
        grade_label = tk.Label(popup, text="Grade You Want to Get (Ex: 75,89,95):")
        grade_label.grid(row=0, column=0, padx=10, pady=5)
        grade_entry = tk.Entry(popup)
        grade_entry.grid(row=0, column=1, padx=10, pady=5)
        '''
        grade_label = tk.Label(popup, text="Grade You Want to Get:")
        grade_label.grid(row=0, column=0, padx=10, pady=5)
        grade_options = ["100", "95", "90", "85", "80", "75", "70"]
        grade_var = tk.StringVar()
        grade_var.set(grade_options[0])  # Default value
        grade_dropdown = tk.OptionMenu(popup, grade_var, *grade_options)
        grade_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Dropdown menu for grade types
        weight_type_label = tk.Label(popup, text="Grade Type to Focus On:")
        weight_type_label.grid(row=1, column=0, padx=10, pady=5)
        weight_types = ["Exam", "Quiz", "Homework", "Assignment"]
        weight_type_var = tk.StringVar()
        weight_type_var.set(weight_types[0])  # Default value
        weight_type_dropdown = tk.OptionMenu(popup, weight_type_var, *weight_types)
        weight_type_dropdown.grid(row=1, column=1, padx=10, pady=5)


        def on_submit_button_click(the_class):
            # This function will be called when the "submit" button is clicked
            # Create and display the text widget
            submit_data(the_class)

        # Function to handle submited data
        def submit_data(the_class):
            string_grade = str(grade_var.get())
            intended_grade = int(string_grade)
            selection = weight_type_var.get()

            # Create the text widget based on different grade types
            if selection == "Quiz":
                needed_avg = calc_needed_quiz_avg(intended_grade, the_class)
                # Create quiz text widget
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining quizzes to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Exam":
                needed_avg = calc_needed_exam_avg(intended_grade, the_class)
                # Create exam text widget
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining exams to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Assignment":
                needed_avg = calc_needed_assignment_avg(intended_grade, the_class)
                # Create assignment text widget
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining assignments to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Homework":
                needed_avg = calc_needed_homework_avg(intended_grade, the_class)
                # Create exam text widget
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining homework to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)

        
        # Create and place the submit button
        submit_button = tk.Button(popup, text="Submit", command=on_submit_button_click(the_class))
        submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Create and place the back button
        back_button = tk.Button(popup, text="Back", command=popup.destroy)
        back_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


    # Create the main application window
    root = tk.Tk()
    root.title("Grade Calculator Application")
    root.geometry("750x750")

    button = tk.Button(root, text="A-Calculator", command=on_button_click(the_class), width=10, height=2)
    button.grid(row=0, column=0, padx=10, pady=5)

    root.mainloop()


