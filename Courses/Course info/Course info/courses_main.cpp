// purpose of this file is to call on course_info to gather:
// - user date
// - process data and prepare it for usage/ storage

#include <iostream>
#include "course_info.h"
using namespace std;

int main() {
    // Create an object of CourseInfo
    CourseInfo course;
    course.loadFromFile("course_data.txt");

    // Access public data members
    cout << "Course Name: " << course.courseName << endl;
    cout << "Exam Weight: " << course.examWeight << endl;
    cout << "Homework Weight: " << course.homeworkWeight << endl;
    cout << "Assignment Weight: " << course.assignmentWeight << endl;
    cout << "Quiz Weight: " << course.quizWeight << endl;

    // Save data to file
    course.saveToFile("saved_course_data.txt");

    return 0;
}
