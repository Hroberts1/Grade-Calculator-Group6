#include <iostream>
#include "course_info.h"


using namespace std;


int main() {
    // Create an object of CourseInfo
    CourseInfo course;

    // Prompt the user to input assignment data
    char addAnother;
    do {
        string assignmentName, assignmentType;
        double grade;

        cout << "\nEnter assignment name: ";
        cin >> ws; // Clear the input buffer
        getline(cin, assignmentName);

        cout << "Enter assignment type: ";
        cin >> assignmentType;

        cout << "Enter grade: ";
        cin >> grade;

        // Add the assignment data to the CourseInfo object
        course.addAssignment(assignmentName, assignmentType, grade);

        cout << "\nDo you want to add another assignment? (y/n): ";
        cin >> addAnother;
    } while (addAnother == 'y' || addAnother == 'Y');

    // Save data to file
    course.saveToFile("saved_course_data.txt");

    // Load data from file
    CourseInfo loadedCourse;
    loadedCourse.loadFromFile("saved_course_data.txt");

    // Access public data members
    cout << "\nCourse Name: " << loadedCourse.courseName << endl;
    cout << "Exam Weight: " << loadedCourse.examWeight << endl;
    cout << "Homework Weight: " << loadedCourse.homeworkWeight << endl;
    cout << "Assignment Weight: " << loadedCourse.assignmentWeight << endl;
    cout << "Quiz Weight: " << loadedCourse.quizWeight << endl;

    // Display loaded assignment data
    cout << "\nAssignment Data:" << endl;
    for (const auto& assignment : loadedCourse.assignments) {
        cout << "Assignment Name: " << assignment.assignmentName << ", ";
        cout << "Type: " << assignment.assignmentType << ", ";
        cout << "Grade: " << assignment.grade << endl;
    }

    return 0;
}
