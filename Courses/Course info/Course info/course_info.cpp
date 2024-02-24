#include <iostream>
#include <vector>
#include "course_info.h"

int main() {
    std::vector<CourseInfo> courses;

    char addAnotherCourse;
    do {
        CourseInfo course;

        // Prompt the user to input assignment data
        char addAnotherAssignment;
        do {
            std::string assignmentName, assignmentType;
            double grade;

            std::cout << "\nEnter assignment name: ";
            std::cin >> std::ws; // Clear the input buffer
            std::getline(std::cin, assignmentName);

            std::cout << "Enter assignment type: ";
            std::cin >> assignmentType;

            std::cout << "Enter grade: ";
            std::cin >> grade;

            // Add the assignment data to the CourseInfo object
            course.addAssignment(assignmentName, assignmentType, grade);

            std::cout << "\nDo you want to add another assignment? (y/n): ";
            std::cin >> addAnotherAssignment;
        } while (addAnotherAssignment == 'y' || addAnotherAssignment == 'Y');

        courses.push_back(course);

        std::cout << "\nDo you want to add another course? (y/n): ";
        std::cin >> addAnotherCourse;
    } while ((addAnotherCourse == 'y' || addAnotherCourse == 'Y') && courses.size() < 7); // Maximum 7 courses

    // Save data to file
    std::ofstream file("saved_course_data.txt");
    if (file.is_open()) {
        for (const auto& course : courses) {
            file << "Course Name: " << course.courseName << std::endl;
            file << "Exam Weight: " << course.examWeight << std::endl;
            file << "Homework Weight: " << course.homeworkWeight << std::endl;
            file << "Assignment Weight: " << course.assignmentWeight << std::endl;
            file << "Quiz Weight: " << course.quizWeight << std::endl;

            file << "Assignment Data:" << std::endl;
            for (const auto& assignment : course.assignments) {
                file << "Assignment Name: " << assignment.assignmentName << ", ";
                file << "Type: " << assignment.assignmentType << ", ";
                file << "Grade: " << assignment.grade << std::endl;
            }
            file << std::endl; // Add a newline between courses
        }
        file.close();
        std::cout << "\nData saved to file: saved_course_data.txt" << std::endl;
    }
    else {
        std::cerr << "Unable to open file: saved_course_data.txt" << std::endl;
    }

    return 0;
}
