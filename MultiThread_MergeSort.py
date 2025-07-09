import threading

def merge(arr, left, mid, right):
    """
    Merges two sorted subarrays of arr.
    Left subarray is arr[left:mid+1]
    Right subarray is arr[mid+1:right+1]
    """
    # Create temporary arrays
    left_sub = arr[left:mid+1]
    right_sub = arr[mid+1:right+1]

    i = j = 0  # Initial indexes for left_sub and right_sub
    k = left   # Initial index for merged array

    # Merge temp arrays back into arr[left:right+1]
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    # Copy remaining elements of left_sub (if any)
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1

    # Copy remaining elements of right_sub (if any)
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """
    Standard merge sort algorithm with multithreading applied.
    """
    if left < right:
        mid = (left + right) // 2

        # Create two threads for sorting both halves
        left_thread = threading.Thread(target=merge_sort, args=(arr, left, mid))
        right_thread = threading.Thread(target=merge_sort, args=(arr, mid + 1, right))

        # Start both threads
        left_thread.start()
        right_thread.start()

        # Wait for both threads to finish
        left_thread.join()
        right_thread.join()

        # Merge the sorted halves
        merge(arr, left, mid, right)


def main():
    print("===== Multithreaded Merge Sort =====")

    try:
        input_str = input("Enter a list of integers separated by spaces: ")
        arr = list(map(int, input_str.split()))
    except:
        print("Invalid input. Please enter numbers only.")
        return

    print("\nOriginal array:", arr)

    # Perform multithreaded merge sort
    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted array: ", arr)


if __name__ == "__main__":
    main()
