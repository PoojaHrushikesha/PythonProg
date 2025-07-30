def count_vowels_and_consonants(text):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

def main():
    # Take input from the user
    input_text = input("Enter a string: ")

    # Get counts
    vowels, consonants = count_vowels_and_consonants(input_text)

    # Display the results
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

# Entry point of the program
if __name__ == "__main__":
    main()
