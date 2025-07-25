from shopping_list_manager import display_menu
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def display_item_choices(items):
    print("\nAvailable Items to Add:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

def main():
    shopping_list = []
    available_items = [
        "Milk", "Bread", "Eggs", "Rice", "Sugar", "Salt",
        "Butter", "Apples", "Bananas", "Tomatoes", "Onions", "Chicken"
    ]

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        choice = int(choice)

        if choice == 1:
            # ✅ ADD ITEM FROM A PREDEFINED LIST
            display_item_choices(available_items)
            item_choice = input("Enter the number of the item to add: ").strip()

            if not item_choice.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            item_index = int(item_choice) - 1

            if 0 <= item_index < len(available_items):
                item_to_add = available_items[item_index]
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the shopping list.")
            else:
                print("Invalid item number. Please try again.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
