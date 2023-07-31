#Make sure each business logic is denoted with appropriate comments and
#make your code interactive and represent clean and clear output on your
#console screen.

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks


def add_marks(students):
    print("\n--- Add Marks ---")
    roll_number = int(input("Enter the student's roll number: "))
    name = input("Enter the student's name: ")
    marks = float(input("Enter the student's marks: "))

    student = Student(roll_number, name, marks)
    students.append(student)
    print("Marks added successfully!")


def view_all_students(students):
    print("\n--- All Students ---")
    for student in students:
        print(f"Roll Number: {student.roll_number}, Name: {student.name}, Marks: {student.marks}")
    print()


def counselor_menu():
    # Business logic for counselor role (if needed)
    pass


def faculty_menu():
    students = []

    while True:
        print("\nFaculty Menu:")
        print("1. Add marks to students")
        print("2. View all students")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_marks(students)
        elif choice == 2:
            view_all_students(students)
        elif choice == 3:
            print("Exiting faculty menu.")
            break
        else:
            print("Invalid choice. Please try again.")


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
            
        else:
            print("Invalid role choice. Please try again.")


if __name__ == "__main__":
    main()
