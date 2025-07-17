def odd_even_sort(arr):
    """
    Sorts the given array using the Odd-Even Sort algorithm.
    
    Args:
        arr (list): The list to be sorted (in-place)
        
    Returns:
        list: The sorted array
    """
    n = len(arr)
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        
        # Odd phase: Compare and swap odd-indexed elements
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
                
        # Even phase: Compare and swap even-indexed elements
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
                
    return arr

def get_user_input():
    """
    Gets array input from the user.
    
    Returns:
        list: The user-provided array
    """
    print("Enter numbers separated by spaces:")
    user_input = input()
    try:
        return [int(num) for num in user_input.split()]
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return get_user_input()

def main():
    """
    Main function to demonstrate the Odd-Even Sort algorithm.
    """
    print("Odd-Even Sort Algorithm")
    print("-----------------------")
    
    # Example with predefined array
    example_array = [34, 2, 10, -9, 7, 5, 22, -1, 6, 8]
    print("\nExample with predefined array:")
    print(f"Original array: {example_array}")
    sorted_array = odd_even_sort(example_array.copy())
    print(f"Sorted array:   {sorted_array}")
    
    # Example with user input
    print("\nNow try with your own numbers!")
    user_array = get_user_input()
    if user_array:
        print(f"\nYour original array: {user_array}")
        sorted_user_array = odd_even_sort(user_array.copy())
        print(f"Sorted array:       {sorted_user_array}")

if __name__ == "__main__":
    main()
