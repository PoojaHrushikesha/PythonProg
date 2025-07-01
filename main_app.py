import sys

def calculator_app():
    print("\n--- Calculator App ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input")


def todo_app():
    print("\n--- To-Do List App ---")
    todos = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit To-Do App")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task:P ")
            todos.append(task)
        elif choice == '2':
            print("\nYour Tasks:")
            for i, task in enumerate(todos, start=1):
                print(f"{i}. {task}")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


def notes_app():
    print("\n--- Notes App ---")
    notes = {}
    while True:
        print("\n1. Create Note\n2. View Notes\n3. Exit Notes App")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            notes[title] = body
        elif choice == '2':
            for title, body in notes.items():
                print(f"\nTitle: {title}\nNote: {body}")
        elif choice == '3':
            break
        else:
            print("Invalid choice")


def main():
    apps = {
        '1': ("Calculator", calculator_app),
        '2': ("To-Do List", todo_app),
        '3': ("Notes", notes_app),
        '4': ("Exit", None)
    }

    while True:
        print("\n=== Main Console Application ===")
        for key, (name, _) in apps.items():
            print(f"{key}. {name}")
        choice = input("Select an application: ")

        if choice in apps:
            if choice == '4':
                print("Exiting Main Application.")
                break
            else:
                apps[choice][1]()  # Run the selected app function
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

