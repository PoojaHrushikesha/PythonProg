import heapq

def get_nth_highest_orders(customer_orders, n):
    """
    Returns the Nth highest number of orders from a dictionary of customer orders.
    
    Args:
        customer_orders (dict): Dictionary with customer IDs as keys and order counts as values
        n (int): The rank to find (1st highest, 2nd highest, etc.)
        
    Returns:
        int: The Nth highest order count
    """
    if not customer_orders:
        return None
        
    if n <= 0 or n > len(customer_orders):
        return None
        
    # Get all order counts
    order_counts = list(customer_orders.values())
    
    # Use a max heap approach to efficiently find Nth highest
    # We convert to negative numbers to simulate a max heap using heapq (which is min heap by default)
    max_heap = [-x for x in order_counts]
    heapq.heapify(max_heap)
    
    nth_highest = None
    for _ in range(n):
        nth_highest = -heapq.heappop(max_heap)
        
    return nth_highest

def generate_sample_data():
    """
    Generates sample customer order data.
    
    Returns:
        dict: Sample customer orders with customer IDs as keys and order counts as values
    """
    return {
        "C1001": 15,
        "C1002": 42,
        "C1003": 27,
        "C1004": 12,
        "C1005": 35,
        "C1006": 42,  # Tie with C1002
        "C1007": 8,
        "C1008": 19,
        "C1009": 35,  # Tie with C1005
        "C1010": 23
    }

def main():
    """
    Main function to demonstrate finding the Nth highest order count.
    """
    print("Customer Order Analysis Program")
    print("-------------------------------")
    
    # Get sample data
    customer_orders = generate_sample_data()
    
    # Display all customer orders sorted
    print("\nAll Customer Orders (sorted by order count):")
    sorted_orders = sorted(customer_orders.items(), key=lambda x: (-x[1], x[0]))
    for customer, orders in sorted_orders:
        print(f"{customer}: {orders} orders")
    
    # Get user input for N
    while True:
        try:
            n = int(input("\nEnter N to find the Nth highest order count (1-10): "))
            if 1 <= n <= 10:
                break
            print("Please enter a number between 1 and 10")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Find and display result
    result = get_nth_highest_orders(customer_orders, n)
    
    if result is not None:
        # Find all customers with this order count
        customers_with_nth = [cust for cust, orders in customer_orders.items() if orders == result]
        
        print(f"\nThe {n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'} highest order count is: {result}")
        print("Customers with this order count:")
        for cust in customers_with_nth:
            print(f"- {cust}")
    else:
        print("\nCould not determine the Nth highest order count.")

if __name__ == "__main__":
    main()
