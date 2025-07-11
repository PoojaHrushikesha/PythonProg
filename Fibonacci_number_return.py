def fibonacci(n):
    """
    Returns the nth Fibonacci number using an efficient iterative approach.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    where fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, etc.
    
    Args:
        n (int): The index of the Fibonacci number to return
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    try:
        n = int(input("Enter a non-negative integer to get the nth Fibonacci number: "))
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
