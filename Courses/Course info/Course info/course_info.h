#ifndef COURSEINFO_H
#define COURSEINFO_H

#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;


class AssignmentData {
public:
    // Public properties
    string assignmentName;
    string assignmentType;
    double grade;

    // Public constructor
    AssignmentData(const string& name, const string& type, double grade);

    // Public destructor
    ~AssignmentData();
};

class CourseInfo {
public:
    // Public data members
    string courseName;
    double examWeight;
    double homeworkWeight;
    double assignmentWeight;
    double quizWeight;

    // Vector to hold AssignmentData objects
    vector<AssignmentData> assignments;

    // Public constructor
    CourseInfo();

    // Public destructor
    ~CourseInfo();

    // Function to save data to a file
    void saveToFile(const string& filename);

    // Function to load data from a file
    void loadFromFile(const string& filename);

    // Function to add assignment data
    void addAssignment(const string& name, const string& type, double grade);
};

#endif // COURSEINFO_H
