#when user select option 1 then it will display following menu
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks


def add_student(students):
    print("\n--- Add Student ---")
    roll_number = int(input("Enter the student's roll number: "))
    name = input("Enter the student's name: ")
    marks = float(input("Enter the student's marks: "))

    student = Student(roll_number, name, marks)
    students.append(student)
    print("Student added successfully!")


def remove_student(students):
    print("\n--- Remove Student ---")
    roll_number = int(input("Enter the roll number of the student to remove: "))

    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            print(f"Student with roll number {roll_number} removed successfully.")
            break
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

    for student in students:
        if student.roll_number == roll_number:
            print(f"Roll Number: {student.roll_number}, Name: {student.name}, Marks: {student.marks}")
            break
    else:
        print(f"Student with roll number {roll_number} not found.")


def counselor_menu():
    students = []

    while True:
        print("\n--- Counselor Menu ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Exit Counselor Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student(students)
        elif choice == 2:
            remove_student(students)
        elif choice == 3:
            view_all_students(students)
        elif choice == 4:
            view_specific_student(students)
        elif choice == 5:
            print("Exiting Counselor Menu.")
            break
        else:
            print("Invalid choice. Please try again.")


def faculty_menu():
    # Business logic for faculty role (if needed)
    pass


def student_menu():
    # Business logic for student role (if needed)
    pass


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
            faculty_menu()
        elif role_choice == 3:
            student_menu()
        elif role_choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid role choice. Please try again.")


if __name__ == "__main__":
    main()
