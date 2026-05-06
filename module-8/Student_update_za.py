import json

# ---------------------------------------------------
# Function to print each student in the required format
# ---------------------------------------------------
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , Email = {student['Email']}")
    print()  # blank line for readability


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------
def main():

    # Load JSON file
    with open("student.json", "r") as file:
        student_list = json.load(file)

    print("Original Student List:")
    print_students(student_list)

    # Add your new student entry
    new_student = {
        "F_Name": "Zach",
        "L_Name": "Allen",
        "Student_ID": 99999,
        "Email": "zallen@example.com"
    }

    student_list.append(new_student)

    print("Updated Student List:")
    print_students(student_list)

    # Write updated list back to JSON file
    with open("student.json", "w") as file:
        json.dump(student_list, file, indent=4)

    print("student.json file was updated.")


# Run program
main()