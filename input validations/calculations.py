import sqlite3
import os

def calculate_exact_grade(course_name):
    course_directory = os.path.join("COURSES", course_name.replace(' ', '_'))
    course_db_path = os.path.join(course_directory, f"{course_name.replace(' ', '_')}_assignments.db")

    if not os.path.exists(course_db_path):
        return "No assignments found for this course."

    total_weight = 0
    weighted_sum = 0

    with sqlite3.connect(course_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT assignment_type, assignment_grade FROM assignments''')
        assignments = cursor.fetchall()

        for assignment in assignments:
            assignment_type, assignment_grade = assignment
            weight = get_weight_by_type(course_name, assignment_type)
            if weight is None:
                return f"Weight for assignment type '{assignment_type}' not found in course '{course_name}'."

            total_weight += weight
            weighted_sum += (weight / 100) * float(assignment_grade)

    if total_weight == 0:
        return "No assignment weights found for this course."

    exact_grade = (weighted_sum / total_weight) * 100
    return exact_grade

def get_weight_by_type(course_name, assignment_type):
    course_directory = os.path.join("COURSES", course_name.replace(' ', '_'))
    course_info_db_path = os.path.join(course_directory, f"{course_name.replace(' ', '_')}_info.db")

    with sqlite3.connect(course_info_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT {} FROM course_info'''.format(assignment_type.lower() + '_weight'))
        weight = cursor.fetchone()
        if weight:
            return float(weight[0].strip('%'))
        else:
            return None
