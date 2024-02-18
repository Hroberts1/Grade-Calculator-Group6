#include <vector>

class Course {
private:
    std::string courseName;
    std::vector<Assignment> assignments;

public:
    Course(const std::string& courseName) : courseName(courseName) {}

    // Function to add an assignment
    void addAssignment(const Assignment& assignment) {
        assignments.push_back(assignment);
    }

    // Function to apply weight to assignments
    void applyWeight(double weight, const std::string& type) {
        for (Assignment& assignment : assignments) {
            if (assignment.getType() == type) {
                double weightedGrade = assignment.getGrade() * weight;
                assignment.setGrade(weightedGrade);
            }
        }
    }

    // Other functions to access information about the course or assignments can be added as needed
};
