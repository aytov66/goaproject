# Sequence is just when Python does things one after another, step by step
print("First step")   # This prints first
print("Second step")  # Then this one
print("Third step")   # Then this

# Iteration is like a loop, it repeats stuff
for i in range(3):  # This will do it 3 times
    print("Loop number", i)

# Selection is when the code picks what to do based on something (like if)
age = 14
if age >= 13:
    print("You're a teenager!")  # This prints if the condition is True
else:
    print("You're not a teenager")



# An algorithm is like a list of steps to solve a problem.
# For example, making coffee:
# 1. Boil water
# 2. Put coffee in a cup and add sugar if you'd like
# 3. Pour water
# 4. Enjoy your coffee!

# Ways to show an algorithm:
# - With words (like above)
# - In code (in Python or another language)
# - With pseudocode (like code but not exact)

print(True or False and False or True and False or False and False or False and True and False or True)
# Step 1: Do ands first:
# False and False = False
# True and False = False
# False and False = False
# False and True = False
# True and False = False
# So now it looks like:
# True or False or False or False or False or True
# Do ORs from left to right:
# True or False = True
# True or False = True
# True or False = True
# True or True = True
# Final answer: True

print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)
# Step 1: ANDs first:
# 7 * 7 / 7 == 7 = 49 / 7 == 7 = 7 == 7 = True
# So: True and False -> False
# True and "1234" != "1234" → True and False -> False
# 7 + 3 * 3 + 1 = 7 + 9 + 1 = 17, so 17 == 15 -> False
# Now replace:
# 5 > 10 or False or False or False or False or True
#  False or False or False or False or True = True
# Final answer: True

num = int(input("Enter a number: "))
if (num % 2 == 0 and num > 10) or num == 7:
    print(True)
else:
    print(False)






# int examples
print(int(3.9))     # turns float into int -> 3
print(int("10"))    # turns string into int -> 10
print(int(True))    # True is 1 -> 1

# str examples
print(str(123))     # turns number to string -> '123'
print(str(True))    # ->'True'
print(str(3.14))    # -> '3.14'

# float examples
print(float(5))     # -> 5.0
print(float("8.5")) # -> 8.5
print(float(True))  # -> 1.0

# bool examples
print(bool(0))      # -> False
print(bool("hi"))   # ->True
print(bool(""))     # -> False






year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # a year is a leap year if it is divisible by 4 and not divisible by 100, or if it is divisible by 400
    print("This is leap year")
else:
    print("Not a leap year")