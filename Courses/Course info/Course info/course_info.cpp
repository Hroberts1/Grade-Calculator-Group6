#include "course_info.h"
#include <sstream>

using namespace std;
// Constructor definition
CourseInfo::CourseInfo() {
    // Prompt the user for input
    cout << "Enter the course name: ";
    getline(cin, courseName);

    cout << "Enter the weight for exams: ";
    cin >> examWeight;

    cout << "Enter the weight for homeworks: ";
    cin >> homeworkWeight;

    cout << "Enter the weight for assignments: ";
    cin >> assignmentWeight;

    cout << "Enter the weight for quizzes: ";
    cin >> quizWeight;

    // Ensure the weights add up to 1 (or 100%)
    double totalWeight = examWeight + homeworkWeight + assignmentWeight + quizWeight;
    if (totalWeight != 1.0) {
        cerr << "Error: The total weight must add up to 1.0 (or 100%)." << endl;
        // You can handle this error however you want, e.g., set default values or exit the program
    }

    cin.ignore(); // Ignore newline character after entering the last weight
}

// Destructor definition
CourseInfo::~CourseInfo() {}

// Function to save data to a file
void CourseInfo::saveToFile(const string& filename) {
    ofstream file(filename);
    if (file.is_open()) {
        file << "Course Name: " << courseName << endl;
        file << "Exam Weight: " << examWeight << endl;
        file << "Homework Weight: " << homeworkWeight << endl;
        file << "Assignment Weight: " << assignmentWeight << endl;
        file << "Quiz Weight: " << quizWeight << endl;

        file << "Assignment Data:" << endl;
        for (const auto& assignment : assignments) {
            file << "Assignment Name: " << assignment.assignmentName << ", ";
            file << "Type: " << assignment.assignmentType << ", ";
            file << "Grade: " << assignment.grade << endl;
        }

        file.close();
        cout << "Data saved to file: " << filename << endl;
    }
    else {
        cerr << "Unable to open file: " << filename << endl;
    }
}

// Function to load data from a file
void CourseInfo::loadFromFile(const string& filename) {
    ifstream file(filename);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            if (line.substr(0, 13) == "Assignment Name:") {
                string name, type;
                double grade;
                istringstream iss(line);
                iss.ignore(17); // Ignore "Assignment Name: "
                getline(iss, name, ',');
                iss.ignore(7); // Ignore ", Type: "
                getline(iss, type, ',');
                iss.ignore(8); // Ignore ", Grade: "
                iss >> grade;
                assignments.push_back(AssignmentData(name, type, grade));
            }
        }
        file.close();
        cout << "Data loaded from file: " << filename << endl;
    }
    else {
        cerr << "Unable to open file: " << filename << endl;
    }
}

// Function to add assignment data
void CourseInfo::addAssignment(const string& name, const string& type, double grade) {
    assignments.push_back(AssignmentData(name, type, grade));
}
