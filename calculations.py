# calculations.py
import sqlite3

def calc_avg(course_name, average_type):
    conn = sqlite3.connect(f"{course_name.replace(' ', '_')}_assignments.db")
    c = conn.cursor()

    total_weight = 0
    weighted_sum = 0

    c.execute("SELECT assignment_type, assignment_grade FROM assignments")
    assignments = c.fetchall()

    for assignment_type, grade in assignments:
        weight = get_weight(course_name, assignment_type)
        weighted_sum += float(grade) * weight
        total_weight += weight

    if total_weight == 0:
        return 0  # Avoid division by zero
    else:
        average = weighted_sum / total_weight
        return average if average_type == "class" else get_assignment_type_average(assignments, average_type)

def get_assignment_type_average(assignments, assignment_type):
    total = 0
    count = 0

    for assignment_type_, grade in assignments:
        if assignment_type_ == assignment_type:
            total += float(grade)
            count += 1

    return total / count if count != 0 else 0

def get_weight(course_name, assignment_type):
    conn = sqlite3.connect(f"{course_name.replace(' ', '_')}_info.db")
    c = conn.cursor()

    c.execute("SELECT exam_weight, project_weight, quiz_weight, homework_weight, assignment_weight FROM course_info")
    weights = c.fetchone()

    if assignment_type == "exam":
        return float(weights[0])
    elif assignment_type == "project":
        return float(weights[1])
    elif assignment_type == "quiz":
        return float(weights[2])
    elif assignment_type == "homework":
        return float(weights[3])
    elif assignment_type == "assignment":
        return float(weights[4])
    else:
        return 0
