def basic_unpacking():
    print("=== Basic Tuple Unpacking ===")
    person = ("Alice", 25, "Engineer")
    name, age, profession = person
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Profession: {profession}")
    print()

def unpacking_with_loop():
    print("=== Tuple Unpacking in a Loop ===")
    students = [("John", 85), ("Emma", 92), ("Mike", 78)]
    for name, score in students:
        print(f"{name} scored {score}")
    print()

def unpacking_with_star():
    print("=== Tuple Unpacking with * Operator ===")
    numbers = (1, 2, 3, 4, 5, 6)
    first, *middle, last = numbers
    print(f"First: {first}")
    print(f"Middle: {middle}")
    print(f"Last: {last}")
    print()

def swap_variables():
    print("=== Swapping Variables Using Tuple Unpacking ===")
    a = 10
    b = 20
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After Swap: a = {a}, b = {b}")
    print()

def main():
    basic_unpacking()
    unpacking_with_loop()
    unpacking_with_star()
    swap_variables()

# Entry point
if __name__ == "__main__":
    main()
