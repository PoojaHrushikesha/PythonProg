import random
import time

def roll_dice():
    return random.randint(1, 6)

def main():
    print("====== DICE ROLL SIMULATOR ======\n")

    while True:
        choice = input("Press Enter to roll the dice or 'q' to quit: ").strip().lower()

        if choice == 'q':
            print("\nGoodbye!")
            break

        print("\nRolling the dice...")
        time.sleep(1)

        number = roll_dice()
        print(f"🎲 You rolled: {number}\n")

if __name__ == "__main__":
    main()
