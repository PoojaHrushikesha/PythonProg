#add 2 numbers
num1 = 10.7
num2 = 5
sum = num1 + num2
print(sum)


#swapping numbers

num1 = 5
num2 = 10

print(f"Before swap: num1 = {num1}, num2 = {num2}")
#here f is used when we need to use varibles from the programme
# Swapping using tuple unpacking
num1, num2 = num2, num1

print(f"After swap: num1 = {num1}, num2 = {num2}")

#Odd even programming

num = int(input("Enter a number: "))

if (num % 2) == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

#Finding Largest number out of 3

num1 = 10
num2 = 25
num3 = 15

largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")

#or

num1 = 10
num2 = 25
num3 = 15

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")
