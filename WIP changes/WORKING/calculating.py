# File: calculating.py
# Purpose: This script contains the core logic for calculating grades and generating reports
# based on the data stored in the SQLite databases. It includes functions to compute overall
# grades for courses, generate reports with grade breakdowns, and perform other related calculations.

import os
import sqlite3

def calculate_course_grade(course_directory):
    # Connect to the course_info database
    course_info_db_path = os.path.join(course_directory, "course_info.db")
    course_info_db = sqlite3.connect(course_info_db_path)
    course_info_cursor = course_info_db.cursor()

    # Retrieve weights from course_info
    course_info_cursor.execute("SELECT * FROM course_info")
    course_info = course_info_cursor.fetchone()
    exam_weight, project_weight, homework_weight, quiz_weight, assignment_weight = course_info[1:]

    # Connect to the course_assignments database
    course_assignments_db_path = os.path.join(course_directory, "course_assignments.db")
    course_assignments_db = sqlite3.connect(course_assignments_db_path)
    course_assignments_cursor = course_assignments_db.cursor()

    # Retrieve assignments and grades
    course_assignments_cursor.execute("SELECT * FROM assignments")
    assignments = course_assignments_cursor.fetchall()

    # Calculate weighted grades for each assignment and sum them up
    total_weighted_grade = 0
    for assignment in assignments:
        assignment_name, assignment_type, assignment_grade = assignment
        if assignment_type == "Exam":
            weighted_grade = float(assignment_grade) * (exam_weight / 100)
        elif assignment_type == "Project":
            weighted_grade = float(assignment_grade) * (project_weight / 100)
        elif assignment_type == "Homework":
            weighted_grade = float(assignment_grade) * (homework_weight / 100)
        elif assignment_type == "Quiz":
            weighted_grade = float(assignment_grade) * (quiz_weight / 100)
        elif assignment_type == "Assignment":
            weighted_grade = float(assignment_grade) * (assignment_weight / 100)
        else:
            weighted_grade = 0
        
        total_weighted_grade += weighted_grade

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
    course_directory = "COURSE_BACKBONE/YourCourseDirectory"  # Replace with the actual course directory path
    total_weighted_grade = calculate_course_grade(course_directory)
    letter_grade = determine_letter_grade(total_weighted_grade)
    print(f"Total Weighted Grade: {total_weighted_grade}")
    print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    main()
