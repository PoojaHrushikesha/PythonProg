def quick_sort(arr):
    """
    Sorts a list in ascending order using Quick Sort algorithm.
    
    Args:
        arr (list): The list to be sorted
        
    Returns:
        list: The sorted list
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (here we use the last element)
    pivot = arr[-1]
    
    # Partition the array into three parts
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the left and right partitions
    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    # Example usage
    try:
        # Get input from user
        input_str = input("Enter numbers separated by spaces: ")
        arr = list(map(int, input_str.split()))
        
        # Sort the array
        sorted_arr = quick_sort(arr)
        
        # Display the result
        print("Original array:", arr)
        print("Sorted array:", sorted_arr)
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")

if __name__ == "__main__":
    main()
