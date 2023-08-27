#These application contain two modules 
#Admin
#Pharmacy Manager

class UserRoles:
    ADMIN = "admin"
    PHARMACY_MANAGER = "pharmacy_manager"

from pharmacy.pharmacy_management_system import PharmacyManagementSystem

def main():
    print("Welcome to Pharmacy Management Application")
    user_role = input("Enter your role (admin/pharmacy_manager): ").lower()

    if user_role == "admin":
        pharmacy_system = PharmacyManagementSystem(user_role)
        pharmacy_system.run()
    elif user_role == "pharmacy_manager":
        pharmacy_system = PharmacyManagementSystem(user_role)
        pharmacy_system.run()
    else:
        print("Invalid role. Exiting the application.")

if __name__ == "__main__":
    main()

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
                print("1. Add Medicine")
                # Add more admin-specific options here
            elif self.user_role == UserRoles.PHARMACY_MANAGER:
                print("1. Search Medicine")
                # Add more pharmacy manager-specific options here
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                if self.user_role == UserRoles.ADMIN:
                    self.add_medicine()
                elif self.user_role == UserRoles.PHARMACY_MANAGER:
                    self.search_medicine()
                # Add more role-specific cases here

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def add_medicine(self):
        # Implement the admin-specific add_medicine method here

    def search_medicine(self):
        # Implement the pharmacy manager-specific search_medicine method here

    # ... Other methods ...

    def __del__(self):
        self.cursor.close()
        self.connection.close()
