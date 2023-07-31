#faculty menu as follows.
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks


def add_marks(students):
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


if __name__ == "__main__":
    faculty_menu()
