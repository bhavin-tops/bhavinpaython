#Prepare demonstration of Python pharmacy management application
#under software development principles and follow coding protocols

from pharmacy.pharmacy_management_system import PharmacyManagementSystem

def main():
    pharmacy_system = PharmacyManagementSystem()
    pharmacy_system.run()

if __name__ == "__main__":
    main()

class Medicine:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, medicine):
        self.medicines[medicine.code] = medicine

    def update_stock(self, code, quantity):
        if code in self.medicines:
            self.medicines[code].stock += quantity

    def get_medicine(self, code):
        return self.medicines.get(code)

    def get_medicines(self):
        return self.medicines.values()

from pharmacy.medicine import Medicine, Inventory

class PharmacyManagementSystem:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
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
        code = input("Enter medicine code: ")
        name = input("Enter medicine name: ")
        price = float(input("Enter medicine price: "))
        medicine = Medicine(code, name, price)
        self.inventory.add_medicine(medicine)
        print("Medicine added successfully.")

    def search_medicine(self):
        code = input("Enter medicine code: ")
        medicine = self.inventory.get_medicine(code)
        if medicine:
            print(f"Medicine found - Name: {medicine.name}, Price: {medicine.price}")
        else:
            print("Medicine not found.")

    def update_stock(self):
        code = input("Enter medicine code: ")
        quantity = int(input("Enter quantity to update: "))
        self.inventory.update_stock(code, quantity)
        print("Stock updated.")

    def display_medicines(self):
        medicines = self.inventory.get_medicines()
        print("Medicine List:")
        for medicine in medicines:
            print(f"Code: {medicine.code}, Name: {medicine.name}, Price: {medicine.price}")

