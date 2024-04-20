import sqlite3
import os

def calculate_exact_grade(total_grade, total_weight):
    if total_weight == 0:
        return "No assignment weights found for this course."

    exact_grade = (total_grade / total_weight) * 100
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
