#include "calculator.h"
using namespace std;

double calcAvg(CourseInfo c){
    double quizavg = 0;
    double examavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if(it -> assignmentType == "quiz"){
            quizavg += it->grade;
        }
        else if(it -> assignmentType == "exam"){
            examavg += it->grade;
        }
        else if(it -> assignmentType == "homework"){
            homeworkavg += it->grade;
        }
        else if(it -> assignmentType == "assignment"){
            assignmentavg += it->grade;
        }
    }
    quizavg /= quiznum;
    examavg /= examnum;
    homeworkavg /= homeworknum;
    assignmentavg /= assignmentnum;

    double totavg = quizavg * c.quizWeight + examavg * c.examWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight;
    return totavg;
}

double calcNeededQuizAvg(double grade, CourseInfo c, int totquiznum){
    double examavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int examnum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if(it -> assignmentType == "exam"){
            examavg += it->grade;
        }
        else if(it -> assignmentType == "homework"){
            homeworkavg += it->grade;
        }
        else if(it -> assignmentType == "assignment"){
            assignmentavg += it->grade;
        }
    }
    examavg /= examnum;
    homeworkavg /= homeworknum;
    assignmentavg /= assignmentnum;

    double neededavg = grade - (examavg * c.examWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight);
    neededavg /= totquiznum;

    return neededavg;
}

double calcNeededExamAvg(double grade, CourseInfo c, int totexamnum){
    double quizavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if(it -> assignmentType == "quiz"){
            quizavg += it->grade;
        }
        else if(it -> assignmentType == "homework"){
            homeworkavg += it->grade;
        }
        else if(it -> assignmentType == "assignment"){
            assignmentavg += it->grade;
        }
    }
    quizavg /= quiznum;
    homeworkavg /= homeworknum;
    assignmentavg /= assignmentnum;

    double neededavg = grade - (quizavg * c.quizWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight);
    neededavg /= totexamnum;

    return neededavg;
}

double calcNeededHomeworkAvg(double grade, CourseInfo c, int tothomeworknum){
    double quizavg = 0;
    double examavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if(it -> assignmentType == "quiz"){
            quizavg += it->grade;
        }
        else if(it -> assignmentType == "exam"){
            examavg += it->grade;
        }
        else if(it -> assignmentType == "assignment"){
            assignmentavg += it->grade;
        }
    }
    quizavg /= quiznum;
    examavg /= examnum;
    assignmentavg /= assignmentnum;

    double neededavg = grade - (quizavg * c.quizWeight + examavg * c.examWeight + assignmentavg * c.assignmentWeight);
    neededavg /= tothomeworknum;

    return neededavg;
}

double calcNeededAssignmentAvg(double grade, CourseInfo c, int totassignmentnum){
    double quizavg = 0;
    double examavg = 0;
    double homeworkavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int homeworknum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if(it -> assignmentType == "quiz"){
            quizavg += it->grade;
        }
        else if(it -> assignmentType == "exam"){
            examavg += it->grade;
        }
        else if(it -> assignmentType == "homework"){
            homeworkavg += it->grade;
        }
    }
    quizavg /= quiznum;
    examavg /= examnum;
    homeworkavg /= homeworknum;

    double neededavg = grade - (quizavg * c.quizWeight + examavg * c.examWeight + homeworkavg * c.homeworkWeight);
    neededavg /= totassignmentnum;

    return neededavg;
}