num = input("Please enter a number: ")
if num > 10:
    print("You are right")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)
print("a == b:", a == b)
print("a != b:", a != b)


# if means: if something is true, do this, if it's not true, do something else

score = 80

# if your score is bigger than 70
if score > 70:
    # then print this message
    print("Great job!")           # the message will be printed only if the condition is true
else:
    # if the condition is not true then print this message
    print("try again!") # the message will be printed only if the condition is not true
