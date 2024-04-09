import os

class AssignmentInf:
    def __init__(self, n="", t="", g=0):
        self.type = t
        self.name = n
        self.grade = g

class CourseInf:
    def __init__(self):
        self.courseName = ""
        self.gradeWeight = 0
        self.examWeight = 0
        self.homeworkWeight = 0
        self.assignmentWeight = 0
        self.quizWeight = 0
        self.assignments = []

    def input_info(self):
        self.courseName = input("Enter course name: ")
        self.gradeWeight = float(input("Enter grade weight: "))
        self.examWeight = self.gradeWeight * 0.4  # 40% for exams
        self.homeworkWeight = self.gradeWeight * 0.3  # 30% for homeworks
        self.assignmentWeight = self.gradeWeight * 0.2  # 20% for assignments
        self.quizWeight = self.gradeWeight * 0.1  # 10% for quizzes

    def input_assignment(self):
        assignment_name = input("Enter assignment name: ")
        assignment_type = input("Enter assignment type: ")
        assignment_grade = float(input("Enter assignment grade: "))
        assignment = AssignmentInf(assignment_name, assignment_type, assignment_grade)
        self.assignments.append(assignment)
        self.save_to_file("assignment_data.txt", assignment_name, assignment_type, assignment_grade)

    def display_info(self):
        print("Course Name:", self.courseName)
        print("Grade Weight:", self.gradeWeight)
        print("Exam Weight:", self.examWeight)
        print("Homework Weight:", self.homeworkWeight)
        print("Assignment Weight:", self.assignmentWeight)
        print("Quiz Weight:", self.quizWeight)

    def save_to_file(self, filename, assignment_name, assignment_type, assignment_grade):
        with open(filename, 'a') as file:
            file.write(f"Assignment Name: {assignment_name}, Type: {assignment_type}, Grade: {assignment_grade}\n")
        print(f"Assignment data has been saved to {filename}")

    def save_course_info_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Course Name: {self.courseName}\n")
            file.write(f"Grade Weight: {self.gradeWeight}\n")
            file.write(f"Exam Weight: {self.examWeight}\n")
            file.write(f"Homework Weight: {self.homeworkWeight}\n")
            file.write(f"Assignment Weight: {self.assignmentWeight}\n")
            file.write(f"Quiz Weight: {self.quizWeight}\n")
        print(f"Course information has been saved to {filename}")

    def read_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        else:
            print(f"File {filename} does not exist")

    @staticmethod
    def delete_all_course_data():
        for filename in os.listdir():
            if filename.endswith(".txt"):
                os.remove(filename)
                print(f"Deleted file: {filename}")

# Usage Example:
'''
course = CourseInf()
course.input_info()
course.input_assignment()
course.display_info()
course.save_course_info_to_file("course_data.txt")
course.read_from_file("course_data.txt")
CourseInf.delete_all_course_data()
'''
