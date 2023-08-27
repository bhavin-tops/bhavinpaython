#Make sure Database normalize manage in this project work

# manager.py
class Manager:
    def __init__(self, name, pharmacy_name):
        self.name = name
        self.pharmacy_name = pharmacy_name

    def insert_into_db(self, connection):
        cursor = connection.cursor()
        insert_query = "INSERT INTO Manager (name, pharmacy_name) VALUES (%s, %s)"
        data = (self.name, self.pharmacy_name)
        cursor.execute(insert_query, data)
        connection.commit()
        print("Manager inserted successfully!")

# medicine.py
class Medicine:
    def __init__(self, name, added_date, added_by, price, quantity):
        self.name = name
        self.added_date = added_date
        self.added_by = added_by
        self.price = price
        self.quantity = quantity

    def insert_into_db(self, connection):
        cursor = connection.cursor()
        insert_query = "INSERT INTO Medicine (name, added_date, added_by, price, quantity) VALUES (%s, %s, %s, %s, %s)"
        data = (self.name, self.added_date, self.added_by, self.price, self.quantity)
        cursor.execute(insert_query, data)
        connection.commit()
        print("Medicine inserted successfully!")

# main.py
# ... your main program loop
    if choice == "1":
        name = input("Enter Medicine Name: ")
        added_date = input("Enter Added Date (YYYY-MM-DD): ")
        added_by = int(input("Enter Manager ID: "))  # You would get the manager ID somehow
        price = get_positive_float_input("Enter Price: ")
        qty = input("Enter Quantity: ")

        medicine = Medicine(name, added_date, added_by, price, qty)
        medicine.insert_into_db(connection)
        print("Medicine information inserted into the database.")

    elif choice == "2":
        name = input("Enter Manager Name: ")
        pharmacy_name = input("Enter Pharmacy Name: ")

        manager = Manager(name, pharmacy_name)
        manager.insert_into_db(connection)
        print("Manager information inserted into the database.")
# ...

