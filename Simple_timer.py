import time
import os

def clear_screen():
    # Works on Windows, Mac, Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer_display = f"{mins:02d}:{secs:02d}"
        print("⏳ Timer:", timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\n⏰ Time's up!")

def main():
    clear_screen()
    print("====== SIMPLE TIMER ======\n")

    try:
        seconds = int(input("Enter time in seconds: "))
        if seconds < 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    print("\nStarting timer...\n")
    countdown(seconds)

if __name__ == "__main__":
    main()
