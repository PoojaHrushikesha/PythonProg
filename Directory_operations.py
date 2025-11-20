
def print_menu():
    print("\n====== DICTIONARY OPERATIONS ======")
    print("1. Create dictionary")
    print("2. Add item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Search for a key")
    print("6. Search for a value")
    print("7. Display dictionary")
    print("8. Display keys")
    print("9. Display values")
    print("10. Display items (key-value pairs)")
    print("11. Merge another dictionary")
    print("12. Clear dictionary")
    print("13. Exit")
    print("====================================")

def main():
    my_dict = {}

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        # 1. Create dictionary
        if choice == "1":
            n = int(input("How many items to add? "))
            my_dict = {}
            for i in range(n):
                key = input(f"Enter key {i+1}: ")
                value = input(f"Enter value for '{key}': ")
                my_dict[key] = value
            print("Dictionary created!")

        # 2. Add item
        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print("Item added!")

        # 3. Update item
        elif choice == "3":
            key = input("Enter key to update: ")
            if key in my_dict:
                value = input("Enter new value: ")
                my_dict[key] = value
                print("Value updated!")
            else:
                print("Key not found!")

        # 4. Delete item
        elif choice == "4":
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print("Item deleted!")
            else:
                print("Key not found!")

        # 5. Search for a key
        elif choice == "5":
            key = input("Enter key to search: ")
            if key in my_dict:
                print(f"Found: {key} → {my_dict[key]}")
            else:
                print("Key not found!")

        # 6. Search for a value
        elif choice == "6":
            value = input("Enter value to search: ")
            keys = [k for k, v in my_dict.items() if v == value]
            if keys:
                print(f"Value found in keys: {keys}")
            else:
                print("Value not found!")

        # 7. Display dictionary
        elif choice == "7":
            print("Dictionary:", my_dict)

        # 8. Display keys
        elif choice == "8":
            print("Keys:", list(my_dict.keys()))

        # 9. Display values
        elif choice == "9":
            print("Values:", list(my_dict.values()))

        # 10. Display items
        elif choice == "10":
            print("Items:")
            for k, v in my_dict.items():
                print(f"{k} → {v}")

        # 11. Merge another dictionary
        elif choice == "11":
            new_dict = {}
            n = int(input("How many items to merge? "))
            for i in range(n):
                key = input(f"Enter key {i+1}: ")
                value = input(f"Enter value for '{key}': ")
                new_dict[key] = value
            my_dict.update(new_dict)
            print("Dictionaries merged!")

        # 12. Clear dictionary
        elif choice == "12":
            my_dict.clear()
            print("Dictionary cleared!")

        # 13. Exit
        elif choice == "13":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
