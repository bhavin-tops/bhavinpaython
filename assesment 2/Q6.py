#Pharmacy Manager
#Can Register
#Can Login
#Can Add Medicine
#Can View Medicine
#Can Delete Medicine

import mysql.connector
from pharmacy.medicine import Medicine, UserRoles

class PharmacyManagementSystem:
    def __init__(self, user_role):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="pharmacy_db"
        )
        self.cursor = self.connection.cursor()
        self.user_role = user_role

    def run(self):
        while True:
            print("\nPharmacy Management System")
            if self.user_role == UserRoles.ADMIN:
                # ... Admin options ...
            elif self.user_role == UserRoles.PHARMACY_MANAGER:
                print("1. Add Medicine")
                print("2. View Medicine")
                print("3. Delete Medicine")
                # Add more pharmacy manager-specific options here
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                if self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.add_medicine()

            elif choice == '2':
                if self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.view_medicines()

            elif choice == '3':
                if self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.delete_medicine()

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def add_medicine(self):
        # Implement the add_medicine method for Pharmacy Manager here

    def view_medicines(self):
        # Implement the view_medicines method for Pharmacy Manager here

    def delete_medicine(self):
        # Implement the delete_medicine method for Pharmacy Manager here

    # ... Other methods ...

    def __del__(self):
        self.cursor.close()
        self.connection.close()
