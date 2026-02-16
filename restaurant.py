menu = {
    "pizza": 100,
    "pasta": 50,
    "burger": 70,
    "salad": 70,
    "coffee": 80
}

def show_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item.title()} : Rs {price}")
    print()

def update_price():
    show_menu()
    item = input("Enter item to update price: ").lower()
    if item in menu:
        new_price = int(input("Enter new price: "))
        menu[item] = new_price
        print("Price updated successfully.")
    else:
        print("Item not found.")

def customer_order():
    total = 0
    while True:
        show_menu()
        choice = input("Enter item to order: ").lower()
        if choice in menu:
            total += menu[choice]
            print(f"{choice} added to order.")
        else:
            print("Item not available.")

        more = input("Add more items? (yes/no): ").lower()
        if more != "yes":
            break

    print(f"\nTotal bill: Rs {total}")

print("Welcome to Farhan's Restaurant")

while True:
    print("\n1. Shopkeeper (Update Price)")
    print("2. Customer (Place Order)")
    print("3. Exit")

    option = input("Choose option: ")

    if option == "1":
        update_price()
    elif option == "2":
        customer_order()
    elif option == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")