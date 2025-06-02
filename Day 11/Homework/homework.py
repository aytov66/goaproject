# 1) Print all numbers from 0 to n (inclusive)
n = int(input("Enter a number (n): "))
for i in range(0, n + 1):
    print(i)
print()

# 2) Ask for age and if they have a student card
age = int(input("Enter your age: "))
student_card = input("Do you have a student card? (yes/no): ").lower()

if age < 18 or student_card == "yes":
    print("You get a discount!")
elif age >= 60 and student_card != "yes":
    print("You get a senior discount!")
else:
    print("No discount for you.")
print()

# 3) Ask for two numbers and check positivity
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > 0 and y > 0:
    print("Both numbers are positive")
elif (x > 0 and y <= 0) or (x <= 0 and y > 0):
    print("Only one number is positive")
else:
    print("Neither number is positive")
print()

# 4) Simple calculator
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    print("Result:", a + b)
elif operation == "-":
    print("Result:", a - b)
elif operation == "*":
    print("Result:", a * b)
elif operation == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Invalid operation!")
else:
    print("Invalid operation!")
print()

a = 2 + 3
result_0 = a

b = result_0 * 4
result_1 = b

c = result_1 - 7
result_2 = c

print("result_0:", result_0)
print("result_1:", result_1)
print("result_2:", result_2)