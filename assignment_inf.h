#ifndef ASSIGNMENT_INF_H
#define ASSIGNMENT_INF_H
using namespace std;

class assignment_inf{
public:
    string type;
    string name;
    double grade;
    
    assignment_inf(){
        type = "";
        name = "";
        grade = 0;
    }

    assignment_inf(string n, string t, double g){
        type = t;
        name = n;
        grade = g;
    }
};

#endif 