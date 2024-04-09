import os
import tkinter as tk
from COURSE_INF import CourseInf, AssignmentInf
from CALCULATOR import calc_avg, calc_needed_quiz_avg, calc_needed_exam_avg, calc_needed_assignment_avg, calc_needed_homework_avg

def run_A_Calculator(the_class):
    def on_button_click(the_class):
        create_needed_grade_popup(the_class)

    def create_needed_grade_popup(the_class):
        popup = tk.Toplevel()

        grade_label = tk.Label(popup, text="Grade You Want to Get:")
        grade_label.grid(row=0, column=0, padx=10, pady=5)
        grade_options = ["100", "95", "90", "85", "80", "75", "70"]
        grade_var = tk.StringVar()
        grade_var.set(grade_options[0])
        grade_dropdown = tk.OptionMenu(popup, grade_var, *grade_options)
        grade_dropdown.grid(row=0, column=1, padx=10, pady=5)

        weight_type_label = tk.Label(popup, text="Grade Type to Focus On:")
        weight_type_label.grid(row=1, column=0, padx=10, pady=5)
        weight_types = ["Exam", "Quiz", "Homework", "Assignment"]
        weight_type_var = tk.StringVar()
        weight_type_var.set(weight_types[0])
        weight_type_dropdown = tk.OptionMenu(popup, weight_type_var, *weight_types)
        weight_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

        def on_submit_button_click(the_class):
            submit_data(the_class)

        def submit_data(the_class):
            string_grade = str(grade_var.get())
            intended_grade = int(string_grade)
            selection = weight_type_var.get()

            if selection == "Quiz":
                needed_avg = calc_needed_quiz_avg(intended_grade, the_class)
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining quizzes to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Exam":
                needed_avg = calc_needed_exam_avg(intended_grade, the_class)
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining exams to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Assignment":
                needed_avg = calc_needed_assignment_avg(intended_grade, the_class)
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining assignments to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)
            elif selection == "Homework":
                needed_avg = calc_needed_homework_avg(intended_grade, the_class)
                num_remain_label = tk.Label(popup, text="You need to get an average of " + str(needed_avg) + " on the remaining homework to get a class average of " + string_grade)
                num_remain_label.grid(row=5, column=0, padx=10, pady=5)

        submit_button = tk.Button(popup, text="Submit", command=lambda: on_submit_button_click(the_class))
        submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        back_button = tk.Button(popup, text="Back", command=popup.destroy)
        back_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    root = tk.Tk()
    root.title("Grade Calculator Application")
    root.geometry("750x750")

    button = tk.Button(root, text="A-Calculator", command=lambda: on_button_click(the_class), width=10, height=2)
    button.grid(row=0, column=0, padx=10, pady=5)

    root.mainloop()

def main():
    c1 = CourseInf()
    c1.input_info()
    c1.display_info()
    c1.input_assignment()  # assignment, 60, a1
    c1.input_assignment()  # homework, 70, h2
    c1.input_assignment()  # exam, 85, e1
    c1.input_assignment()  # quiz, 90, q2

    print("reaches GUI...")

    run_A_Calculator(c1)

if __name__ == "__main__":
    main()
