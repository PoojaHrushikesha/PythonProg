import random

def main():
    print("====== NUMBER GUESSING GAME ======\n")
    print("I'm thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100!")
            continue

        if guess < number:
            print("Too low! Try again.\n")
        elif guess > number:
            print("Too high! Try again.\n")
        else:
            print(f"\n🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} attempts.")
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
