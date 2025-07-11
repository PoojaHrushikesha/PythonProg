def find_largest_smallest(arr):
    if not arr:
        return None, None  # Edge case: empty list
    
    # Initialize smallest and largest with first element
    smallest = largest = arr[0]

    # Traverse the list and update smallest and largest
    for num in arr[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return largest, smallest


# ======================
#   Main Program Logic
# ======================

if __name__ == "__main__":
    try:
        # Get user input
        input_str = input("Enter a list of integers separated by spaces: ")
        arr = list(map(int, input_str.strip().split()))

        if not arr:
            print("Error: You entered an empty list.")
        else:
            largest, smallest = find_largest_smallest(arr)
            print(f"\nLargest element: {largest}")
            print(f"Smallest element: {smallest}")
    
    except ValueError:
        print("Invalid input. Please enter only integers.")
