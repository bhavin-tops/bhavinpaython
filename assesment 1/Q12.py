#Make sure code prevent from unexpected exception
#E.g. in contact number users can’t be able to enter character value if.. Enter
#Character value - return to the previous menu and accept all details again.
class Student:
    def __init__(self, roll_number, first_name, last_name, contact, subjects, faculty):
        self.roll_number = roll_number
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.subjects = subjects
        self.faculty = faculty


def add_student(students, roll_number, first_name, last_name, contact, subjects, faculty):
    student = Student(roll_number, first_name, last_name, contact, subjects, faculty)
    students[roll_number] = student


def validate_contact(contact):
    if not contact.isdigit() or len(contact) != 10:
        raise ValueError("Invalid contact number. Please enter a 10-digit numeric value.")


def counselor_menu():
    students = {}

    while True:
        print("\nSelect an option:")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Exit Counselor Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n--- Add Student ---")
            roll_number = int(input("Enter the student's roll number: "))
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            contact = input("Enter the student's contact number: ")

            try:
                validate_contact(contact)
                subjects = {}
                num_subjects = int(input("Enter the number of subjects: "))
                for _ in range(num_subjects):
                    subject_name = input("Enter the subject name: ")
                    marks = int(input("Enter the subject marks: "))
                    fees = int(input("Enter the subject fees: "))
                    subjects[subject_name] = {"marks": marks, "fees": fees}

                faculty = input("Enter the faculty name: ")
                add_student(students, roll_number, first_name, last_name, contact, subjects, faculty)
                print("Student added successfully!")

            except ValueError as e:
                print(str(e))
                print("Returning to the previous menu. Please try again.")

        elif choice == 2:
            # Add remove_student_details() here if needed
            pass
        elif choice == 3:
            # Add view_all_students() here if needed
            pass
        elif choice == 4:
            # Add view_specific_student() here if needed
            pass
        elif choice == 5:
            print("Exiting Counselor Menu.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    counselor_menu()

