'''def highest_product_of_three(arr):
    if len(arr) < 3:
        raise ValueError("Less than 3 items!")

    # Sort the array
    arr.sort()

    # The maximum product is either:
    # 1. Product of the three largest numbers
    # 2. Product of the two smallest numbers and the largest number
    return max(
        arr[-1] * arr[-2] * arr[-3],
        arr[0] * arr[1] * arr[-1]
    )
'''
'''
    arr = [1, 10, 2, 6, -1, -4]
# Highest product of 3: 10 * 6 * 2 = 120
arr = [-10, -10, 5, 2]
# Highest product of 3: (-10) * (-10) * 5 = 500
output:
print(highest_product_of_three([1, 10, 2, 6, -1, -4]))  # Output: 120
print(highest_product_of_three([-10, -10, 5, 2]))        # Output: 500
print(highest_product_of_three([-1, -2, -3, -7]))        # Output: -6 (All negatives)
'''
def highest_product_of_three(arr):
    if len(arr) < 3:
        raise ValueError("The input array must contain at least three numbers.")

    # Initialize the six key values
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        # Update top three maximums
        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num

        # Update bottom two minimums
        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num

    # Calculate the two possible products
    product1 = max1 * max2 * max3  # Three largest positives
    product2 = min1 * min2 * max1  # Two negatives + one positive

    # Return the maximum of the two
    return max(product1, product2)


# ======================
#   Main Program Logic
# ======================

if __name__ == "__main__":
    try:
        # Input: space-separated integers
        input_str = input("Enter a list of integers separated by spaces: ")
        arr = list(map(int, input_str.strip().split()))

        if len(arr) < 3:
            print("Error: At least three integers are required.")
        else:
            result = highest_product_of_three(arr)
            print(f"The highest product of any three integers is: {result}")

    except ValueError:
        print("Invalid input. Please enter only integers.")
