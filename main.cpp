#include <iostream>
#include <vector>
#include "course_inf.h"
#include "calculator.h"

using namespace std;

int main() {
    course_inf* c1 = new course_inf();
    c1->inputInfo();
    c1->displayInfo();
    c1->inputAssignment(); // assignment, 60, a1
    c1->inputAssignment(); // assignment, 100, a2
    c1->inputAssignment(); // homework, 50, h1
    c1->inputAssignment(); // homework, 70, h2
    c1->inputAssignment(); // exam, 85, e1
    c1->inputAssignment(); // quiz, 90, q1
    c1->inputAssignment(); // quiz, 90, q2
    
    /*
    for(auto it = c1->assignments.begin(); it != c1->assignments.end(); it++){
        cout << (*it)->name << " " << (*it)->type << " " << (*it)->grade << endl;
    }
    cout << endl;
    */

    double avg = calcAvg((*c1));
    cout << "Class Average: " << avg << endl;
    double neededquizavg = calcNeededQuizAvg(90, (*c1));
    cout << "Needed Quiz Average: " << neededquizavg << endl;
    double neededexamavg = calcNeededExamAvg(90, (*c1));
    cout << "Needed Exam Average: " << neededexamavg << endl;
    double neededhomeworkavg = calcNeededHomeworkAvg(90, (*c1));
    cout << "Needed Homework Average: " << neededhomeworkavg << endl;
    double neededassignmentavg = calcNeededAssignmentAvg(90, (*c1));
    cout << "Needed Assignment Average: " << neededassignmentavg << endl;
    
    return 0;
}
