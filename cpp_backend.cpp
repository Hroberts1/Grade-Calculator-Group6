#include <iostream>
#include <fstream>
#include <sstream>
#include <string>


// Function to process the course data passed from Python
void processCourseData(const std::string& courseName, const std::string& examWeight,
                       const std::string& projectWeight, const std::string& quizWeight,
                       const std::string& homeworkWeight, const std::string& assignmentWeight) {
    // Create a separate file for each course
    std::ofstream courseFile(courseName + ".txt");
    if (!courseFile.is_open()) {
        std::cerr << "Error: Unable to create course file for " << courseName << std::endl;
        return;
    }

    // Write course data to the file
    courseFile << "Course Name: " << courseName << std::endl;
    courseFile << "Exam Weight: " << examWeight << std::endl;
    courseFile << "Project Weight: " << projectWeight << std::endl;
    courseFile << "Quiz Weight: " << quizWeight << std::endl;
    courseFile << "Homework Weight: " << homeworkWeight << std::endl;
    courseFile << "Assignment Weight: " << assignmentWeight << std::endl;

    // Close the file
    courseFile.close();

    std::cout << "Course data written to file: " << courseName + ".txt" << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 7) {
        std::cerr << "Usage: " << argv[0] << " <course_name> <exam_weight> <project_weight> <quiz_weight> <homework_weight> <assignment_weight>" << std::endl;
        return 1;
    }

    // Extract course data from command-line arguments
    std::string courseName = argv[1];
    std::string examWeight = argv[2];
    std::string projectWeight = argv[3];
    std::string quizWeight = argv[4];
    std::string homeworkWeight = argv[5];
    std::string assignmentWeight = argv[6];

    // Process course data
    processCourseData(courseName, examWeight, projectWeight, quizWeight, homeworkWeight, assignmentWeight);

    return 0;
}
