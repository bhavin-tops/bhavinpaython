#Program should not be terminated till the user Exit it

from db_connection import DatabaseConnector
from medicine import Medicine
from manager import Manager

def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_medicine(connection):
    name = input("Enter Medicine Name: ")
    added_date = input("Enter Added Date (YYYY-MM-DD): ")
    added_by = int(input("Enter Manager ID: "))  # You would get the manager ID somehow
    price = get_positive_float_input("Enter Price: ")
    qty = input("Enter Quantity: ")

    medicine = Medicine(name, added_date, added_by, price, qty)
    medicine.insert_into_db(connection)
    print("Medicine information inserted into the database.")
    print()

def add_manager(connection):
    name = input("Enter Manager Name: ")
    pharmacy_name = input("Enter Pharmacy Name: ")

    manager = Manager(name, pharmacy_name)
    manager.insert_into_db(connection)
    print("Manager information inserted into the database.")
    print()

def delete_question(connection):
    question_id = int(input("Enter Question ID to delete: "))
    confirm = input(f"Are you sure you want to delete question {question_id}? (Y/N): ").lower()

    if confirm == "y":
        # Implement the deletion logic here (e.g., SQL DELETE query)
        # Print appropriate message after deletion
        print(f"Question {question_id} has been deleted.")
    else:
        print("Deletion canceled.")

def main():
    db_connector = DatabaseConnector('localhost', 'your_username', 'your_password', 'pharmacy_db')
    db_connector.connect()

    while True:
        print("Select an option:")
        print("1. Add Medicine")
        print("2. Add Manager")
        print("3. Delete Question")
        print("4. Exit")

        choice = input()

        if choice == "1":
            add_medicine(db_connector.get_connection())

        elif choice == "2":
            add_manager(db_connector.get_connection())

        elif choice == "3":
            delete_question(db_connector.get_connection())

        elif choice == "4":
            print("Thank you for using the pharmacy system!")
            break  # Exit the loop and terminate the program

        else:
            print("Invalid choice. Please select again.")
            print()

    db_connector.disconnect()

if __name__ == "__main__":
    main()
