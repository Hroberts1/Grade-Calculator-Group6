// This is our main driver for our code.
#include <QApplication>
#include <QWidget>
#include <QPushButton>
#include <QFileDialog>
#include <QMessageBox>
#include <fstream>
#include <iostream>

// Define your Assignment and Course classes here...

class Application : public QWidget {
    Q_OBJECT

private:
    std::vector<Course> courses;

public:
    Application(QWidget *parent = nullptr)
        : QWidget(parent) {

        // Create a button for saving data
        QPushButton *saveButton = new QPushButton("Save Data", this);
        saveButton->setGeometry(50, 50, 200, 30);

        // Connect the button's clicked signal to the saveData slot
        connect(saveButton, &QPushButton::clicked, this, &Application::saveData);

        // Read from "saved_data.dat" on application start
        readSavedData();
    }

    void readSavedData() {
        std::ifstream file("saved_data.dat");
        if (file.is_open()) {
            // Read data from the file and populate courses vector
            // Example: Read course name, assignments, etc.
            // courses.push_back(/* Construct Course object from file data */);
            std::cout << "Data loaded from saved_data.dat" << std::endl;
            file.close();
        } else {
            std::cerr << "Unable to open saved_data.dat" << std::endl;
        }
    }

public slots:
    void saveData() {
        QString fileName = QFileDialog::getSaveFileName(this, "Save File", "", "Data Files (*.dat)");

        if (!fileName.isEmpty()) {
            std::ofstream file(fileName.toStdString());
            if (file.is_open()) {
                // Write data to the file
                // Example: Write course name, assignments, etc.
                // for (const auto& course : courses) {
                //     // Write course data to file
                // }
                std::cout << "Data saved to " << fileName.toStdString() << std::endl;
                file.close();
            } else {
                QMessageBox::critical(this, "Error", "Unable to open file for writing.");
            }
        }
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    Application window;
    window.resize(300, 200);
    window.setWindowTitle("Grade Calculator");

    window.show();

    return app.exec();
}

#include "main.moc"
