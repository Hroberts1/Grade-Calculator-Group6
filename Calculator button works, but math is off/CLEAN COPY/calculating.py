# File: calculating.py
# Purpose: This script contains the core logic for calculating grades and generating reports
# based on the data stored in the SQLite databases. It includes functions to compute overall
# grades for courses, generate reports with grade breakdowns, and perform other related calculations.

import os
import sqlite3



import os
import sqlite3

def calculate_course_grade(course_name, course_directory):
    # Dynamically generate the database file name based on the course name
    course_info_db_path = os.path.join(course_directory, f"{course_name}_info.db")

    # Connect to the course_info database
    course_info_db = sqlite3.connect(course_info_db_path)
    course_info_cursor = course_info_db.cursor()

    # Retrieve weights from course_info
    course_info_cursor.execute("SELECT * FROM course_info")
    course_info = course_info_cursor.fetchone()
    exam_weight, project_weight, homework_weight, quiz_weight, assignment_weight = course_info[1:]

    # Connect to the course_assignments database
    course_assignments_db_path = os.path.join(course_directory, f"{course_name}_assignments.db")
    course_assignments_db = sqlite3.connect(course_assignments_db_path)
    course_assignments_cursor = course_assignments_db.cursor()

    # Retrieve assignments and grades
    course_assignments_cursor.execute("SELECT * FROM assignments")
    assignments = course_assignments_cursor.fetchall()

    # Calculate weighted grades for each assignment and sum them up
    total_weighted_grade = 0
    exam_avg = 0
    exam_num = 0
    assignment_avg = 0
    assignment_num = 0
    homework_avg = 0
    homework_num = 0
    quiz_avg = 0
    quiz_num = 0
    project_avg = 0
    project_num = 0
    for assignment in assignments:
        assignment_name, assignment_type, assignment_grade = assignment
        if assignment_type == "Exam":
            exam_avg += assignment_grade
            exam_num += 1
            # weighted_grade = float(assignment_grade) * (exam_weight / 100)
        elif assignment_type == "Project":
            project_avg += assignment_grade
            project_num += 1
            # weighted_grade = float(assignment_grade) * (project_weight / 100)
        elif assignment_type == "Homework":
            homework_avg += assignment_grade
            homework_num += 1
            # weighted_grade = float(assignment_grade) * (homework_weight / 100)
        elif assignment_type == "Quiz":
            quiz_avg += assignment_grade
            quiz_num += 1
            # weighted_grade = float(assignment_grade) * (quiz_weight / 100)
        elif assignment_type == "Other":
            assignment_avg += assignment_grade
            assignment_num += 1
            # weighted_grade = float(assignment_grade) * (assignment_weight / 100)

    # Calculate class average, make sure there is no division by zero
    # Calculate exam avgerage
    if exam_num != 0:
        exam_avg /= exam_num
    else:
        exam_avg = 0

    # Calculate quiz avgerage
    if quiz_num != 0:
        quiz_avg /= quiz_num
    else:
        quiz_avg = 0

    # Calculate homework avgerage
    if homework_num != 0:
        homework_avg /= homework_num
    else:
        homework_avg = 0

    # Calculate project avgerage
    if project_num != 0:
        project_avg /= project_num
    else:
        project_avg = 0

    # Calculate assignment avgerage
    if assignment_num != 0:
        assignment_avg /= assignment_num
    else:
        assignment_avg = 0
    
    total_weighted_grade = exam_avg * (exam_weight / 100) + quiz_avg * (quiz_weight / 100) + homework_avg * (homework_weight / 100) + project_avg * (project_weight / 100) + assignment_avg * (assignment_weight / 100)
    
    # Close database connections
    course_info_db.close()
    course_assignments_db.close()

    return total_weighted_grade

def determine_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def main():
    course_name = "YourCourseName"  # Replace with the actual course name
    course_directory = "COURSE_BACKBONE"  # Replace with the actual course directory path
    total_weighted_grade = calculate_course_grade(course_name, course_directory)
    letter_grade = determine_letter_grade(total_weighted_grade)
    print(f"Total Weighted Grade: {total_weighted_grade}")
    print(f"Letter Grade: {letter_grade}")


if __name__ == "__main__":
    main()
