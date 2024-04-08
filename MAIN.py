from COURSE_INF import CourseInf
from CALCULATOR import calc_avg, calc_needed_quiz_avg, calc_needed_exam_avg, calc_needed_homework_avg, calc_needed_assignment_avg

def main():
    c1 = CourseInf()
    c1.input_info()
    c1.display_info()
    c1.input_assignment()  # assignment, 60, a1
    c1.input_assignment()  # assignment, 100, a2
    c1.input_assignment()  # homework, 50, h1
    c1.input_assignment()  # homework, 70, h2
    c1.input_assignment()  # exam, 85, e1
    c1.input_assignment()  # quiz, 90, q1
    c1.input_assignment()  # quiz, 90, q2

    '''
    for assignment in c1.assignments:
        print(assignment.name, assignment.type, assignment.grade)
    print()
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

if __name__ == "__main__":
    main()
