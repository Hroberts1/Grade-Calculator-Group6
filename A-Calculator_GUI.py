# Python program to create a table

import tkinter as tk

def on_button_click():
    # This function will be called when the "A-Calculator" button is clicked
    # Create and display the pop-up window for adding a course
    create_needed_grade_popup()



def create_needed_grade_popup():
    # Create the pop-up window
    popup = tk.Toplevel()

    # Create labels and entry widgets for course name and weights
    grade_label = tk.Label(popup, text="Grade You Want to Get (Ex: 75,89,95):")
    grade_label.grid(row=0, column=0, padx=10, pady=5)
    grade_entry = tk.Entry(popup)
    grade_entry.grid(row=0, column=1, padx=10, pady=5)

    # Dropdown menu for grade types
    weight_type_label = tk.Label(popup, text="Grade Type to Focus On:")
    weight_type_label.grid(row=1, column=0, padx=10, pady=5)
    weight_types = ["Exam", "Quiz", "Homework", "Assignment"]
    weight_type_var = tk.StringVar()
    weight_type_var.set(weight_types[0])  # Default value
    weight_type_dropdown = tk.OptionMenu(popup, weight_type_var, *weight_types)
    weight_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

    num_remain_label = tk.Label(popup, text="Number Remaining(EX: 1 exam remaining):")
    num_remain_label.grid(row=2, column=0, padx=10, pady=5)
    num_remain_entry = tk.Entry(popup)
    num_remain_entry.grid(row=2, column=1, padx=10, pady=5)

    def on_submit_button_click():
        # This function will be called when the "submit" button is clicked
        # Create and display the text widget
        submit_data()

    # Function to handle submited data
    def submit_data():
        selection = weight_type_var.get()
        # Create a text widget
        num_remain_label = tk.Label(popup, text="You need to get an average of XXX on the remaining " + selection + " to get a class average of " + grade_entry.get())
        num_remain_label.grid(row=5, column=0, padx=10, pady=5)
        
        calc_data = {
            "Grade": grade_entry.get(),
            "Num_Remain": num_remain_entry.get(),
        }
    
    # Create and place the submit button
    submit_button = tk.Button(popup, text="Submit", command=on_submit_button_click)
    submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Create and place the back button
    back_button = tk.Button(popup, text="Back", command=popup.destroy)
    back_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


# Create the main application window
root = tk.Tk()
root.title("Grade Calculator Application")
root.geometry("750x750")

button = tk.Button(root, text="A-Calculator", command=on_button_click, width=10, height=2)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()