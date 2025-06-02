i = 0
while i < 10:   # this repearts the loop while i is less than 10
    print(i + 1) 
    i = i + 1 
print()

i = 10
while i > 0: # this repeats the loop while i is greater than 0
    print(i)
    i = i - 1 # this subtracts 1 from i
print()
while True: # this loop makes the user input their password and it wont stop until the password is correct
    password = input("Enter your password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Incorrect password")

print()
n = int(input("Enter a number:")) # this asks the user to enter a number and converts it to an integer
i = 1
total = 0
while i <=n: # this loop adds all the numbers from 1 to n while i is less than or equal to n
    total = total + i
    i = i + 1
print("Sum of numbers from 1 to", n, "is", total)