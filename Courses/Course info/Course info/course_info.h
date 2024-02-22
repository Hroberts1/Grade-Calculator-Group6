#ifndef COURSE_INFO_H
#define COURSE_INFO_H

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class CourseInfo {
public:
    // Public data members
    string courseName;
    double examWeight;
    double homeworkWeight;
    double assignmentWeight;
    double quizWeight;

    // Public constructor
    CourseInfo();

    // Public destructor
    ~CourseInfo();

    // Function to save data to a file
    void saveToFile(const string& filename);

    // Function to load data from a file
    void loadFromFile(const string& filename);
};

#endif // COURSE_INFO_H
