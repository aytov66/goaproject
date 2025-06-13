# 1) infinite while loop
while True:
    print("forever loop")
    break # this will break the loop
# 2) ask the user for their name and print it 10 times
name = input("What's your name? ")
count = 0
while count < 10:
    print("Hello " + name + "!")
    count = count + 1

# 3) while loop with head and body

# this is the head – we're starting with i equal to 0
i = 0

# still part of the head – this says "keep looping while i is less than 5"
while i < 5:
    # this is the body – this is what actually happens each time the loop runs
    print("Looping... i =", i)

    # still in the body – we're adding 1 to i so it eventually hits 5 and stops
    i += 1


# 4) keep asking the user for a number until it's more than 100
num = int(input("Enter a number: "))
while num <= 100:
    print("that's too small, try again!")
    num = int(input("Enter a number: "))
print("Nice! That one's over 100")


# 5) Ask the user to enter 5 different names and store them in a variable, separated by commas

names = ""  # this will hold all the names
count = 0

while count < 5:
    name = input("Enter a name: ")

    if count == 0:
        names = name  # first name, don't add a comma
    else:
        names = names + ", " + name  # add a comma before adding the next name

    count += 1  # move to the next round

print("All the names you entered: " + names)
