#ifndef CALCULATOR_H
#define CALCULATOR_H
#include "course_info.h"
using namespace std;

double calcAvg(CourseInfo c);

double calcNeededQuizAvg(double grade, CourseInfo c, int totquiznum);

double calcNeededExamAvg(double grade, CourseInfo c, int totexamnum);

double calcNeededHomeworkAvg(double grade, CourseInfo c, int tothomeworknum);

double calcNeededAssignmentAvg(double grade, CourseInfo c, int totassignmentnum);

#endif 