
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))

def print_menu():
    print("\n====== TEMPERATURE CONVERTER ======")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("===================================")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            c = float(input("Enter Celsius: "))
            print(f"Fahrenheit = {c_to_f(c):.2f}")

        elif choice == "2":
            c = float(input("Enter Celsius: "))
            print(f"Kelvin = {c_to_k(c):.2f}")

        elif choice == "3":
            f = float(input("Enter Fahrenheit: "))
            print(f"Celsius = {f_to_c(f):.2f}")

        elif choice == "4":
            f = float(input("Enter Fahrenheit: "))
            print(f"Kelvin = {f_to_k(f):.2f}")

        elif choice == "5":
            k = float(input("Enter Kelvin: "))
            print(f"Celsius = {k_to_c(k):.2f}")

        elif choice == "6":
            k = float(input("Enter Kelvin: "))
            print(f"Fahrenheit = {k_to_f(k):.2f}")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
