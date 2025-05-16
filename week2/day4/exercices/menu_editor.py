from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Restaurant Menu Editor ---")
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        print("Exit (E)")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("\nExiting. Here’s the final menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    name = input("Enter item name: ").strip()
    price = input("Enter item price: ").strip()

    try:
        price = int(price)
        item = MenuItem(name, price)
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def remove_item_from_menu():
    name = input("Enter item name to delete: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Item not found. Could not delete.")

def update_item_from_menu():
    old_name = input("Enter current item name: ").strip()
    old_item = MenuManager.get_by_name(old_name)
    if old_item:
        new_name = input("Enter new name: ").strip()
        new_price = input("Enter new price: ").strip()
        try:
            new_price = int(new_price)
            old_item.update(new_name, new_price)
            print("Item was updated successfully.")
        except Exception as e:
            print(f"Error updating item: {e}")
    else:
        print("Item not found. Could not update.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\n--- Restaurant Menu ---")
    if not items:
        print("Menu is empty.")
    else:
        for item in items:
            print(f"{item.name} - ${item.price}")

def view_item():
    name = input("Enter item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item found: {item.name} - ${item.price}")
    else:
        print("Item not found.")

if __name__ == "__main__":
    show_user_menu()
