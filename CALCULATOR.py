from COURSE_INF import CourseInf, AssignmentInf

def calc_avg(c, average_type):
    quiz_avg = 0
    exam_avg = 0
    homework_avg = 0
    assignment_avg = 0
    quiz_num = 0
    exam_num = 0
    homework_num = 0
    assignment_num = 0

    for assignment in c.assignments:
        if assignment.type == "quiz":
            quiz_avg += assignment.grade
            quiz_num += 1
        elif assignment.type == "exam":
            exam_avg += assignment.grade
            exam_num += 1
        elif assignment.type == "homework":
            homework_avg += assignment.grade
            homework_num += 1
        elif assignment.type == "assignment":
            assignment_avg += assignment.grade
            assignment_num += 1

    quiz_avg /= quiz_num
    exam_avg /= exam_num
    homework_avg /= homework_num
    assignment_avg /= assignment_num

    total_avg = (quiz_avg * c.quizWeight + exam_avg * c.examWeight +
                 homework_avg * c.homeworkWeight + assignment_avg * c.assignmentWeight)
    
    if average_type == "quiz":
        return quiz_avg
    elif average_type == "assignment":
        return assignment_avg
    elif average_type == "exam":
        return exam_avg
    elif average_type == "homework":
        return homework_avg
    elif average_type == "class":
        return total_avg


def calc_needed_quiz_avg(grade, c):
    exam_avg = 0
    homework_avg = 0
    assignment_avg = 0
    exam_num = 0
    homework_num = 0
    assignment_num = 0

    for assignment in c.assignments:
        if assignment.type == "exam":
            exam_avg += assignment.grade
            exam_num += 1
        elif assignment.type == "homework":
            homework_avg += assignment.grade
            homework_num += 1
        elif assignment.type == "assignment":
            assignment_avg += assignment.grade
            assignment_num += 1

    exam_avg /= exam_num
    homework_avg /= homework_num
    assignment_avg /= assignment_num

    needed_avg = grade - (exam_avg * c.examWeight + homework_avg * c.homeworkWeight + assignment_avg * c.assignmentWeight)
    needed_avg /= c.quizWeight
    return needed_avg


def calc_needed_exam_avg(grade, c):
    quiz_avg = 0
    homework_avg = 0
    assignment_avg = 0
    quiz_num = 0
    homework_num = 0
    assignment_num = 0

    for assignment in c.assignments:
        if assignment.type == "quiz":
            quiz_avg += assignment.grade
            quiz_num += 1
        elif assignment.type == "homework":
            homework_avg += assignment.grade
            homework_num += 1
        elif assignment.type == "assignment":
            assignment_avg += assignment.grade
            assignment_num += 1

    quiz_avg /= quiz_num
    homework_avg /= homework_num
    assignment_avg /= assignment_num

    needed_avg = grade - (quiz_avg * c.quizWeight + homework_avg * c.homeworkWeight + assignment_avg * c.assignmentWeight)
    needed_avg /= c.examWeight
    return needed_avg


def calc_needed_homework_avg(grade, c):
    quiz_avg = 0
    exam_avg = 0
    assignment_avg = 0
    quiz_num = 0
    exam_num = 0
    assignment_num = 0

    for assignment in c.assignments:
        if assignment.type == "quiz":
            quiz_avg += assignment.grade
            quiz_num += 1
        elif assignment.type == "exam":
            exam_avg += assignment.grade
            exam_num += 1
        elif assignment.type == "assignment":
            assignment_avg += assignment.grade
            assignment_num += 1

    quiz_avg /= quiz_num
    exam_avg /= exam_num
    assignment_avg /= assignment_num

    needed_avg = grade - (quiz_avg * c.quizWeight + exam_avg * c.examWeight + assignment_avg * c.assignmentWeight)
    needed_avg /= c.homeworkWeight
    return needed_avg


def calc_needed_assignment_avg(grade, c):
    quiz_avg = 0
    exam_avg = 0
    homework_avg = 0
    quiz_num = 0
    exam_num = 0
    homework_num = 0

    for assignment in c.assignments:
        if assignment.type == "quiz":
            quiz_avg += assignment.grade
            quiz_num += 1
        elif assignment.type == "exam":
            exam_avg += assignment.grade
            exam_num += 1
        elif assignment.type == "homework":
            homework_avg += assignment.grade
            homework_num += 1

    quiz_avg /= quiz_num
    exam_avg /= exam_num
    homework_avg /= homework_num

    needed_avg = grade - (quiz_avg * c.quizWeight + exam_avg * c.examWeight + homework_avg * c.homeworkWeight)
    needed_avg /= c.assignmentWeight
    return needed_avg
