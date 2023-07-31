#create separate file for all business logics and make them reusable - use
#modules concepts for implements above logic
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks


def add_student(students, roll_number, name, marks):
    student = Student(roll_number, name, marks)
    students.append(student)


def remove_student(students, roll_number):
    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            return True
    return False


def get_all_students(students):
    return students


def get_specific_student(students, roll_number):
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None
import student_logic


def add_student_details(students):
    print("\n--- Add Student ---")
    roll_number = int(input("Enter the student's roll number: "))
    name = input("Enter the student's name: ")
    marks = float(input("Enter the student's marks: "))

    student_logic.add_student(students, roll_number, name, marks)
    print("Student added successfully!")


def remove_student_details(students):
    print("\n--- Remove Student ---")
    roll_number = int(input("Enter the roll number of the student to remove: "))

    if student_logic.remove_student(students, roll_number):
        print(f"Student with roll number {roll_number} removed successfully.")
    else:
        print(f"Student with roll number {roll_number} not found.")


def view_all_students(students):
    print("\n--- All Students ---")
    for student in students:
        print(f"Roll Number: {student.roll_number}, Name: {student.name}, Marks: {student.marks}")
    print()


def view_specific_student(students):
    print("\n--- View Specific Student ---")
    roll_number = int(input("Enter the roll number of the student to view: "))

    student = student_logic.get_specific_student(students, roll_number)
    if student:
        print(f"Roll Number: {student.roll_number}, Name: {student.name}, Marks: {student.marks}")
    else:
        print(f"Student with roll number {roll_number} not found.")
import counselor_logic

def counselor_menu():
    students = []

    while True:
        print("\nSelect an option:")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Exit Counselor Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            counselor_logic.add_student_details(students)
        elif choice == 2:
            counselor_logic.remove_student_details(students)
        elif choice == 3:
            counselor_logic.view_all_students(students)
        elif choice == 4:
            counselor_logic.view_specific_student(students)
        elif choice == 5:
            print("Exiting Counselor Menu.")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\nSelect your role:")
        print("1. Counselor")
        print("2. Faculty")
        print("3. Student")
        print("4. Exit")

        role_choice = int(input("Enter your role choice: "))

        if role_choice == 1:
            counselor_menu()
        elif role_choice == 2:
            # Add faculty_menu() here if needed
            pass
        elif role_choice == 3:
            # Add student_menu() here if needed
            pass
        elif role_choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid role choice. Please try again.")


if __name__ == "__main__":
    main()
