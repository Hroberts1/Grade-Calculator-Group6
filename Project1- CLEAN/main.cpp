#include <iostream>
#include <vector>
#include "course_inf.h"

using namespace std;

void displayMenu() {
    cout << "Menu:" << endl;
    cout << "1. Add a course" << endl;
    cout << "2. View all courses" << endl;
    cout << "3. Delete all course data" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter your choice: ";
}

void displayCourseMenu(const vector<course_inf>& courses) {
    cout << "Courses:" << endl;
    for (size_t i = 0; i < courses.size(); ++i) {
        cout << i + 1 << ". " << courses[i].courseName << endl;
    }
    cout << "Enter course number to view details (0 to go back): ";
}

int main() {
    vector<course_inf> courses;
    int choice;

    do {
        displayMenu();
        cin >> choice;

        switch (choice) {
        case 1: {
            course_inf course;
            course.inputInfo();
            courses.push_back(course);
            break;
        }
        case 2: {
            displayCourseMenu(courses);
            int courseChoice;
            cin >> courseChoice;
            if (courseChoice >= 1 && courseChoice <= courses.size()) {
                courses[courseChoice - 1].displayInfo();
            }
            break;
        }
        case 3: {
            // Delete all course data
            for (auto& course : courses) {
                course.deleteAllCourseData();
            }
            cout << "All course data deleted." << endl;
            break;
        }
        case 4: {
            cout << "Exiting program." << endl;
            break;
        }
        default:
            cout << "Invalid choice. Please enter a number between 1 and 4." << endl;
            break;
        }

    } while (choice != 4);

    return 0;
}
