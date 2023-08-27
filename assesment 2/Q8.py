# Accept all values dynamically

import sqlite3

# Connect to the database (create a new file if not exists)
conn = sqlite3.connect('pharmacy_management.db')
cursor = conn.cursor()

# Create the Medicine table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Medicine (
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity TEXT,
        added_date TEXT,
        added_by INTEGER,
        price REAL
    )
''')

# Create the Manager table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Manager (
        id INTEGER PRIMARY KEY,
        name TEXT,
        pharmacy_name TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

import sqlite3

def add_medicine():
    name = input("Enter Medicine Name: ")
    quantity = input("Enter Quantity: ")
    added_date = input("Enter Added Date (YYYY-MM-DD): ")
    added_by = int(input("Enter Added By (Manager ID): "))
    price = float(input("Enter Price: "))

    conn = sqlite3.connect('pharmacy_management.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Medicine (name, quantity, added_date, added_by, price)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, quantity, added_date, added_by, price))

    conn.commit()
    conn.close()

def add_manager():
    name = input("Enter Manager Name: ")
    pharmacy_name = input("Enter Pharmacy Name: ")

    conn = sqlite3.connect('pharmacy_management.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Manager (name, pharmacy_name)
        VALUES (?, ?)
    ''', (name, pharmacy_name))

    conn.commit()
    conn.close()

while True:
    print("Select an option:")
    print("1. Add Medicine")
    print("2. Add Manager")
    print("3. Exit")
    
    choice = int(input())
    
    if choice == 1:
        add_medicine()
    elif choice == 2:
        add_manager()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select again.")
