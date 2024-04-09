import sqlite3

def calc_avg(course_name, average_type):
    # Connect to the database
    conn = sqlite3.connect(f"{course_name.replace(' ', '_')}_assignments.db")
    cursor = conn.cursor()

    # Execute the SQL query to fetch assignment grades
    cursor.execute("SELECT assignment_type, assignment_grade FROM assignments")
    fetched_assignments = cursor.fetchall()

    # Process the fetched assignments and calculate the average
    total_grade = 0
    total_weight = 0
    for assignment_type, assignment_grade in fetched_assignments:
        if assignment_type.lower() == average_type.lower():
            total_grade += float(assignment_grade)
            total_weight += get_assignment_weight(course_name, assignment_type)

    # Close the database connection
    conn.close()

    # Avoid division by zero
    if total_weight != 0:
        return total_grade / total_weight
    else:
        return None

def get_assignment_weight(course_name, assignment_type):
    # Connect to the database
    conn = sqlite3.connect(f"{course_name.replace(' ', '_')}_info.db")
    cursor = conn.cursor()

    # Execute the SQL query to fetch the weight for the given assignment type
    cursor.execute("SELECT {}_weight FROM course_info".format(assignment_type.lower()))
    weight = cursor.fetchone()[0]

    # Close the database connection
    conn.close()

    return float(weight)
