def count_word_frequency(text):
    # Convert the string to lowercase and split into words
    words = text.lower().split()

    # Initialize an empty dictionary to store word counts
    word_freq = {}

    for word in words:
        # Remove punctuation from each word
        word = word.strip(".,!?\"'()[]{}:;")
        # Update word count in dictionary
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

def main():
    # Take input from user
    input_text = input("Enter a sentence or paragraph: ")

    # Count word frequency
    frequencies = count_word_frequency(input_text)

    # Display the results
    print("\nWord Frequency:")
    for word, count in frequencies.items():
        print(f"{word}: {count}")

# Entry point of the program
if __name__ == "__main__":
    main()
