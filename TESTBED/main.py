# main.pyw
# Purpose: Backbone for the program, handling inputs and importing from other files

import os
import design
import calculating

COURSE_BACKBONE_DIR = "COURSE_BACKBONE"

def create_course_backbone_directory(course_name):
    """
    Create the COURSE_BACKBONE directory if it doesn't exist,
    and create a subdirectory for the given course.
    """
    if not os.path.exists(COURSE_BACKBONE_DIR):
        os.makedirs(COURSE_BACKBONE_DIR)
        print(f"Directory '{COURSE_BACKBONE_DIR}' created successfully.")

    course_dir = os.path.join(COURSE_BACKBONE_DIR, course_name)
    if not os.path.exists(course_dir):
        os.makedirs(course_dir)
        print(f"Subdirectory '{course_name}' created successfully.")
    

def main():
    # Create the COURSE_BACKBONE directory if it doesn't exist
    create_course_backbone_directory("")

    # Start the main menu
    design.main()

if __name__ == "__main__":
    main()
