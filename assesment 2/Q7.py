#Admin
#Can register
#Can Login
#Can View all manager
#Can View al medicine

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
                print("1. Register Manager")
                print("2. View All Managers")
                print("3. View All Medicines")
                # Add more admin-specific options here
            elif self.user_role == UserRoles.PHARMACY_MANAGER:
                print("1. Add Medicine")
                print("2. View Medicines")
                # Add more pharmacy manager-specific options here
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                if self.user_role == UserRoles.ADMIN:
                    self.register_manager()
                elif self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.add_medicine()

            elif choice == '2':
                if self.user_role == UserRoles.ADMIN:
                    self.view_managers()
                elif self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.view_medicines()

            elif choice == '3':
                if self.user_role == UserRoles.ADMIN:
                    self.view_medicines()

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    # ... Other methods ...

    def register_manager(self):
        # Implement the register_manager method for Admin here

    def view_managers(self):
        # Implement the view_managers method for Admin here

    def view_medicines(self):
        # Implement the view_medicines method for Admin and Pharmacy Manager here

    # ... Other methods ...

    def __del__(self):
        self.cursor.close()
        self.connection.close()
