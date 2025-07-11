def heapify(arr, n, i):
    """
    To max heapify a subtree rooted at index i.
    :param arr: List representing the heap
    :param n: Size of the heap
    :param i: Index of the root
    """
    largest = i              # Initialize largest as root
    left = 2 * i + 1         # Left child index
    right = 2 * i + 2        # Right child index

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree


def heap_sort(arr):
    """
    Perform heap sort on the given array.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        heapify(arr, i, 0)  # Heapify the reduced heap


# ======================
#   Main Program Logic
# ======================

if __name__ == "__main__":
    try:
        # Input: space-separated integers
        input_str = input("Enter a list of integers separated by spaces: ")
        arr = list(map(int, input_str.strip().split()))

        print("\nOriginal array:", arr)

        # Perform heap sort
        heap_sort(arr)

        print("Sorted array (ascending order):", arr)

    except ValueError:
        print("Invalid input. Please enter only integers.")
