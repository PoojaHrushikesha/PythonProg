import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")
"""
        import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print(random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(random_float)

# Choose a random element from a list
my_list = ['apple', 'banana', 'cherry']
random_element = random.choice(my_list)
print(random_element)

# Shuffle a list in place
random.shuffle(my_list)
print(my_list)
"""
