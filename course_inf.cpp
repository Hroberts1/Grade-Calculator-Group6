#include "course_inf.h"
#include <iostream>
#include <string>
#include <vector>
#include <cstdio> // For remove() function
//#include <windows.h> // For WinAPI


using namespace std;


// Constructor definition
course_inf::course_inf() {
    vector<assignment_inf*> vec; // added by rx
    assignments = vec; // added by rx
}

// Public member function definition to input course information
void course_inf::inputInfo() {
    cout << "Enter course name: ";
    getline(cin, courseName);

    cout << "Enter grade weight: ";
    cin >> gradeWeight;

    // Calculate individual weights based on overall grade weight
    examWeight = gradeWeight * 0.4; // 40% for exams
    homeworkWeight = gradeWeight * 0.3; // 30% for homeworks
    assignmentWeight = gradeWeight * 0.2; // 20% for assignments
    quizWeight = gradeWeight * 0.1; // 10% for quizzes
}

// Public member function definition to input assignment data
void course_inf::inputAssignment() {
    string assignmentName;
    string assignmentType;
    double assignmentGrade;
    assignment_inf* assignment;

    cin.ignore(); // Clear the newline character left in the input buffer

    cout << "Enter assignment name: ";
    getline(cin, assignmentName);

    cout << "Enter assignment type: ";
    getline(cin, assignmentType);

    cout << "Enter assignment grade: ";
    cin >> assignmentGrade;

    assignment_inf* a = new assignment_inf(assignmentName, assignmentType, assignmentGrade); // added by rx
    assignments.push_back(a); // added by rx

    ofstream outFile("assignment_data.txt", ios::app); // Append mode

    if (outFile.is_open()) {
        outFile << "Assignment Name: " << assignmentName << ", Type: " << assignmentType << ", Grade: " << assignmentGrade << endl;
        outFile.close();
        cout << "Assignment data has been saved to assignment_data.txt" << endl;
    }
    else {
        cerr << "Unable to open file for writing: course_data.txt" << endl;
    }
}

// Public member function definition to display course information
void course_inf::displayInfo() const {
    cout << "Course Name: " << courseName << endl;
    cout << "Grade Weight: " << gradeWeight << endl;
    cout << "Exam Weight: " << examWeight << endl;
    cout << "Homework Weight: " << homeworkWeight << endl;
    cout << "Assignment Weight: " << assignmentWeight << endl;
    cout << "Quiz Weight: " << quizWeight << endl;
}

// Public member function definition to save course information to a file
void course_inf::saveToFile(const string& filename) {
    ofstream outFile(filename);

    if (outFile.is_open()) {
        outFile << "Course Name: " << courseName << endl;
        outFile << "Grade Weight: " << gradeWeight << endl;
        outFile << "Exam Weight: " << examWeight << endl;
        outFile << "Homework Weight: " << homeworkWeight << endl;
        outFile << "Assignment Weight: " << assignmentWeight << endl;
        outFile << "Quiz Weight: " << quizWeight << endl;

        outFile.close();
        cout << "Course information has been saved to " << filename << endl;
    }
    else {
        cerr << "Unable to open file for writing: " << filename << endl;
    }
}

// Public member function definition to read course information from a file
void course_inf::readFromFile(const string& filename) {
    ifstream inFile(filename);

    if (inFile.is_open()) {
        string line;
        while (getline(inFile, line)) {
            cout << line << endl;
        }

        inFile.close();
    }
    else {
        cerr << "Unable to open file for reading: " << filename << endl;
    }
}

/*
void course_inf::deleteAllCourseData() {
    WIN32_FIND_DATAA findFileData;
    HANDLE hFind = FindFirstFileA("*", &findFileData);
    if (hFind != INVALID_HANDLE_VALUE) {
        do {
            if ((findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) == 0 &&
                strstr(findFileData.cFileName, ".txt")) {
                std::string filename = findFileData.cFileName;
                std::remove(filename.c_str());
                std::cout << "Deleted file: " << filename << std::endl;
            }
        } while (FindNextFileA(hFind, &findFileData) != 0);
        FindClose(hFind);
    }
    assignments.clear(); // added by rx
}
*/