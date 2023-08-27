#In this application all operations using MySQL queries

import mysql.connector
from pharmacy.medicine import Medicine

class PharmacyManagementSystem:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="pharmacy_db"
        )
        self.cursor = self.connection.cursor()

    # ... Other methods ...

    def add_medicine(self):
        code = input("Enter medicine code: ")
        name = input("Enter medicine name: ")
        price = float(input("Enter medicine price: "))
        
        # Insert the medicine into the database
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

    # ... Other methods ...

    def __del__(self):
        self.cursor.close()
        self.connection.close()
