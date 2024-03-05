#ifndef CALCULATOR_H
#define CALCULATOR_H
#include "course_inf.h"
using namespace std;

double calcAvg(course_inf c);

double calcNeededQuizAvg(double grade, course_inf c);

double calcNeededExamAvg(double grade, course_inf c);

double calcNeededHomeworkAvg(double grade, course_inf c);

double calcNeededAssignmentAvg(double grade, course_inf c);

#endif 
