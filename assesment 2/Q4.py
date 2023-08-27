#Make sure each business logic is denoted with appropriate comments and
#make your code interactive and represent clean and clear output on your
#console screen.

class Medicine:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.medicines = {}

    # ... Other methods ...
import mysql.connector
from pharmacy.medicine import Medicine

class PharmacyManagementSystem:
    def __init__(self):
        # Initialize database connection
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="pharmacy_db"
        )
        self.cursor = self.connection.cursor()

    def run(self):
        while True:
            # Display menu options
            print("\nPharmacy Management System")
            print("1. Add Medicine")
            print("2. Search Medicine")
            print("3. Update Stock")
            print("4. Display Medicines")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_medicine()

            elif choice == '2':
                self.search_medicine()

            elif choice == '3':
                self.update_stock()

            elif choice == '4':
                self.display_medicines()

            elif choice == '5':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    def add_medicine(self):
        # Gather medicine details
        code = input("Enter medicine code: ")
        name = input("Enter medicine name: ")
        price = float(input("Enter medicine price: "))
        
        # Insert medicine into the database
        insert_query = "INSERT INTO medicines (code, name, price) VALUES (%s, %s, %s)"
        values = (code, name, price)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        
        print("Medicine added successfully.")

    def search_medicine(self):
        code = input("Enter medicine code: ")
        
        # Retrieve medicine from the database
        select_query = "SELECT name, price FROM medicines WHERE code = %s"
        self.cursor.execute(select_query, (code,))
        medicine_data = self.cursor.fetchone()
        
        if medicine_data:
            name, price = medicine_data
            print(f"Medicine found - Name: {name}, Price: {price}")
        else:
            print("Medicine not found.")

    def update_stock(self):
        # ... Implement the update_stock method ...

    def display_medicines(self):
        # ... Implement the display_medicines method ...

    def __del__(self):
        # Close the cursor and connection
        self.cursor.close()
        self.connection.close()
