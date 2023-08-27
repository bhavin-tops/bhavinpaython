#Write a program to demonstrate the application pharmacy management system

class Medicine:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

class PharmacyManagementSystem:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, code, name, price, stock):
        medicine = Medicine(code, name, price, stock)
        self.medicines.append(medicine)

    def search_medicine(self, code):
        for medicine in self.medicines:
            if medicine.code == code:
                return medicine
        return None

    def update_stock(self, code, quantity):
        medicine = self.search_medicine(code)
        if medicine:
            medicine.stock += quantity
            print(f"Stock updated for {medicine.name}. New stock: {medicine.stock}")
        else:
            print("Medicine not found.")

    def display_medicines(self):
        print("Medicine List:")
        for medicine in self.medicines:
            print(f"Code: {medicine.code}, Name: {medicine.name}, Price: {medicine.price}, Stock: {medicine.stock}")

def main():
    pharmacy = PharmacyManagementSystem()

    while True:
        print("\nPharmacy Management System")
        print("1. Add Medicine")
        print("2. Search Medicine")
        print("3. Update Stock")
        print("4. Display Medicines")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter medicine code: ")
            name = input("Enter medicine name: ")
            price = float(input("Enter medicine price: "))
            stock = int(input("Enter initial stock: "))
            pharmacy.add_medicine(code, name, price, stock)
            print("Medicine added successfully.")

        elif choice == '2':
            code = input("Enter medicine code: ")
            medicine = pharmacy.search_medicine(code)
            if medicine:
                print(f"Medicine found - Name: {medicine.name}, Price: {medicine.price}, Stock: {medicine.stock}")
            else:
                print("Medicine not found.")

        elif choice == '3':
            code = input("Enter medicine code: ")
            quantity = int(input("Enter quantity to update: "))
            pharmacy.update_stock(code, quantity)

        elif choice == '4':
            pharmacy.display_medicines()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
