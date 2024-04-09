from COURSE_INF import CourseInf
import tkinter as tk
# from ClassAverage_UI import on_button_click
from A_Calculator_GUI import run_A_Calculator

def main():
    c1 = CourseInf()
    c1.input_info()
    c1.display_info()
    c1.input_assignment()  # assignment, 60, a1
    c1.input_assignment()  # homework, 70, h2
    c1.input_assignment()  # exam, 85, e1
    c1.input_assignment()  # quiz, 90, q2

    
    print("reaches GUI...")

    # Testing Class Average
    '''
    # Create the main application window
    root = tk.Tk()
    root.title("Grade Calculator Application")
    root.geometry("750x750")

    button = tk.Button(root, text="Class Average", command=on_button_click(c1), width=15, height=2)
    button.grid(row=0, column=0, padx=10, pady=5)

    root.mainloop()
    '''
    # Testing A-Calculator
    run_A_Calculator(c1)
    '''
    # Create the main application window
    root = tk.Tk()
    root.title("Grade Calculator Application")
    root.geometry("750x750")

    button = tk.Button(root, text="A-Calculator", command=run_A_Calculator(c1), width=10, height=2)
    button.grid(row=0, column=0, padx=10, pady=5)

    root.mainloop()
    '''
    

    '''
    avg = calc_avg(c1)
    print("Class Average:", avg)
    needed_quiz_avg = calc_needed_quiz_avg(90, c1)
    print("Needed Quiz Average:", needed_quiz_avg)
    needed_exam_avg = calc_needed_exam_avg(90, c1)
    print("Needed Exam Average:", needed_exam_avg)
    needed_homework_avg = calc_needed_homework_avg(90, c1)
    print("Needed Homework Average:", needed_homework_avg)
    needed_assignment_avg = calc_needed_assignment_avg(90, c1)
    print("Needed Assignment Average:", needed_assignment_avg)
    '''
    

if __name__ == "__main__":
    main()
