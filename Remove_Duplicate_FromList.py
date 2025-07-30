def remove_duplicates(input_list):
    # Using a set to remove duplicates while preserving order
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

def main():
    # Take input from user and convert to a list
    raw_input = input("Enter list elements separated by spaces: ")
    input_list = raw_input.split()

    # Remove duplicates
    result = remove_duplicates(input_list)

    # Display the result
    print("List after removing duplicates:")
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()
