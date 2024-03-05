#pragma once
#ifndef COURSE_INF_H
#define COURSE_INF_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector> // added by rx
#include "assignment_inf.h" // added by rx

using namespace std;

class course_inf {
public:
    // Public member variables
    std::string courseName;
    double gradeWeight;
    double examWeight;
    double homeworkWeight;
    double assignmentWeight;
    double quizWeight;
    vector<assignment_inf*> assignments; // added by rx

    // Constructor declaration
    course_inf();

    // Public member function to input course information
    void inputInfo();

    // Public member function to input assignment data
    void inputAssignment();

    // Public member function to display course information
    void displayInfo() const;

    // Public member function to save course information to a file
    void saveToFile(const std::string& filename);

    // Public member function to read course information from a file
    void readFromFile(const std::string& filename);

    // Public member to delete all .txt files made by
    // Program
    void deleteAllCourseData();
};

#endif
