#Implement common fields using inheritance concepts only and make it more
#readable. Medicine qty field must be private only manager can access this field

import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to the database")
        except mysql.connector.Error as err:
            print("Error:", err)
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")
    
    def get_connection(self):
        return self.connection

class CommonFields:
    def __init__(self, name, added_date, added_by, price):
        self.name = name
        self.added_date = added_date
        self.added_by = added_by
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Added Date: {self.added_date}")
        print(f"Added By: {self.added_by}")
        print(f"Price: {self.price}")

from base_classes import CommonFields

class Medicine(CommonFields):
    def __init__(self, name, added_date, added_by, price, qty):
        super().__init__(name, added_date, added_by, price)
        self.__qty = qty  # Private attribute for quantity

    def display_info(self):
        super().display_info()
        print(f"Quantity: {self.__qty}")

    def get_qty(self, manager):
        if isinstance(manager, Manager):
            return self.__qty
        else:
            print("Only managers can access quantity.")
            return None

from base_classes import CommonFields

class Manager(CommonFields):
    def __init__(self, name, added_date, added_by, price, pharmacy_name):
        super().__init__(name, added_date, added_by, price)
        self.pharmacy_name = pharmacy_name

from db_connection import DatabaseConnector
from medicine import Medicine
from manager import Manager

def main():
    db_connector = DatabaseConnector('localhost', 'your_username', 'your_password', 'pharmacy_db')
    db_connector.connect()

    medicine = Medicine("Den p 10X10", "8/6/2022", "Manager A", 20, "10X10")
    manager = Manager("Ramesh", "8/6/2022", "Admin", 0, "Jayraj Pharmacy")

    medicine.display_info()
    manager.display_info()

    qty = medicine.get_qty(manager)
    if qty is not None:
        print(f"Medicine Quantity: {qty}")

    db_connector.disconnect()

if __name__ == "__main__":
    main()
