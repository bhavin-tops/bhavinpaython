#Make sure validation proper given – each options - display appropriate
#message if user enter invalid input and accept values again and again - use
#looping concepts and string inbuilt methods concepts in this logic
#implementation

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

def main():
    db_connector = DatabaseConnector('localhost', 'your_username', 'your_password', 'pharmacy_db')
    db_connector.connect()

    while True:
        print("Select an option:")
        print("1. Add Medicine")
        print("2. Add Manager")
        print("3. Exit")
        
        choice = input()
        
        if choice == "1":
            name = input("Enter Medicine Name: ")
            added_date = input("Enter Added Date (YYYY-MM-DD): ")
            added_by = input("Enter Added By: ")
            price = get_positive_float_input("Enter Price: ")
            qty = input("Enter Quantity: ")
            
            medicine = Medicine(name, added_date, added_by, price, qty)
            medicine.display_info()

            qty_manager = Manager("Manager for Quantity Validation", "8/6/2022", "Admin", 0, "Pharmacy")
            validated_qty = medicine.get_qty(qty_manager)

            if validated_qty is not None:
                print(f"Validated Medicine Quantity: {validated_qty}")

        elif choice == "2":
            name = input("Enter Manager Name: ")
            added_date = input("Enter Added Date (YYYY-MM-DD): ")
            added_by = input("Enter Added By: ")
            price = get_positive_float_input("Enter Price: ")
            pharmacy_name = input("Enter Pharmacy Name: ")

            manager = Manager(name, added_date, added_by, price, pharmacy_name)
            manager.display_info()

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select again.")

    db_connector.disconnect()

if __name__ == "__main__":
    main()
