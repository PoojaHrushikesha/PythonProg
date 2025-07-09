def binary_search(arr, target):
    """
    Perform binary search to find the index of 'target' in a sorted array 'arr'.
    
    Parameters:
        arr (list): A sorted list of elements.
        target: The element to search for.
        
    Returns:
        int: Index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow

        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is greater than mid, search right half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller than mid, search left half
        else:
            right = mid - 1

    # Target not found
    return -1


def main():
    print("===== Binary Search Implementation =====")
    
    # Input sorted array
    try:
        arr = list(map(int, input("Enter a sorted list of integers separated by spaces: ").split()))
    except:
        print("Invalid input for array.")
        return

    # Input target value
    try:
        target = int(input("Enter the target number to search for: "))
    except:
        print("Invalid input for target.")
        return

    # Perform binary search
    result = binary_search(arr, target)

    # Output result
    if result != -1:
        print(f"✅ Target {target} found at index {result}.")
    else:
        print(f"❌ Target {target} not found in the array.")


if __name__ == "__main__":
    main()
