#pragma once
#ifndef ASSIGNMENT_DATA_H
#define ASSIGNMENT_DATA_H

#include <string>

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

#endif // ASSIGNMENT_DATA_H


