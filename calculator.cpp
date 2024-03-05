#include "calculator.h"
using namespace std;

double calcAvg(course_inf c){
    double quizavg = 0;
    double examavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if((*it) -> type == "quiz"){
            quizavg += (*it)->grade;
            quiznum += 1;
        }
        else if((*it) -> type == "exam"){
            examavg += (*it)->grade;
            examnum += 1;
        }
        else if((*it) -> type == "homework"){
            homeworkavg += (*it)->grade;
            homeworknum += 1;
        }
        else if((*it) -> type == "assignment"){
            assignmentavg += (*it)->grade;
            assignmentnum += 1;
        }
    }
    quizavg /= quiznum;
    // cout << "quizavg: " << quizavg << endl;
    examavg /= examnum;
    // cout << "examnum: " << examavg << endl;
    homeworkavg /= homeworknum;
    // cout << "homeworkavg: " << homeworkavg << endl;
    assignmentavg /= assignmentnum;
    // cout << "assignmentavg: " << assignmentavg << endl;

    double totavg = quizavg * c.quizWeight + examavg * c.examWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight;
    return totavg;
}

double calcNeededQuizAvg(double grade, course_inf c){
    double examavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int examnum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if((*it) -> type == "exam"){
            examavg += (*it)->grade;
            examnum += 1;
        }
        else if((*it) -> type == "homework"){
            homeworkavg += (*it)->grade;
            homeworknum += 1;
        }
        else if((*it) -> type == "assignment"){
            assignmentavg += (*it)->grade;
            assignmentnum += 1;
        }
    }
    examavg /= examnum;
    // cout << "examnum: " << examavg << endl;
    homeworkavg /= homeworknum;
    // cout << "homeworkavg: " << homeworkavg << endl;
    assignmentavg /= assignmentnum;
    // cout << "assignmentavg: " << assignmentavg << endl;

    double neededavg = grade - (examavg * c.examWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight);
    // cout << "Needed Total: " << neededavg << endl;
    neededavg /= c.quizWeight;
    return neededavg;
}

double calcNeededExamAvg(double grade, course_inf c){
    double quizavg = 0;
    double homeworkavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int homeworknum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if((*it) -> type == "quiz"){
            quizavg += (*it)->grade;
            quiznum += 1;
        }
        else if((*it) -> type == "homework"){
            homeworkavg += (*it)->grade;
            homeworknum += 1;
        }
        else if((*it) -> type == "assignment"){
            assignmentavg += (*it)->grade;
            assignmentnum += 1;
        }
    }
    quizavg /= quiznum;
    homeworkavg /= homeworknum;
    assignmentavg /= assignmentnum;

    double neededavg = grade - (quizavg * c.quizWeight + homeworkavg * c.homeworkWeight + assignmentavg * c.assignmentWeight);
    neededavg /= c.examWeight;

    return neededavg;
}

double calcNeededHomeworkAvg(double grade, course_inf c){
    double quizavg = 0;
    double examavg = 0;
    double assignmentavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int assignmentnum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if((*it) -> type == "quiz"){
            quizavg += (*it)->grade;
            quiznum += 1;
        }
        else if((*it) -> type == "exam"){
            examavg += (*it)->grade;
            examnum += 1;
        }
        else if((*it) -> type == "assignment"){
            assignmentavg += (*it)->grade;
            assignmentnum += 1;
        }
    }
    quizavg /= quiznum;
    examavg /= examnum;
    assignmentavg /= assignmentnum;

    double neededavg = grade - (quizavg * c.quizWeight + examavg * c.examWeight + assignmentavg * c.assignmentWeight);
    neededavg /= c.homeworkWeight;

    return neededavg;
}

double calcNeededAssignmentAvg(double grade, course_inf c){
    double quizavg = 0;
    double examavg = 0;
    double homeworkavg = 0;
    int quiznum = 0;
    int examnum = 0;
    int homeworknum = 0;

    for(auto it = c.assignments.begin(); it != c.assignments.end(); it++){
        if((*it) -> type == "quiz"){
            quizavg += (*it)->grade;
            quiznum += 1;
        }
        else if((*it) -> type == "exam"){
            examavg += (*it)->grade;
            examnum += 1;
        }
        else if((*it) -> type == "homework"){
            homeworkavg += (*it)->grade;
            homeworknum += 1;
        }
    }
    quizavg /= quiznum;
    examavg /= examnum;
    homeworkavg /= homeworknum;

    double neededavg = grade - (quizavg * c.quizWeight + examavg * c.examWeight + homeworkavg * c.homeworkWeight);
    neededavg /= c.assignmentWeight;

    return neededavg;
}
