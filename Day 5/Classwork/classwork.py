name = input("Whats your name? ")
print(name[0])

str1 = input("Where are you from?")
str2 = input("Whats your last name?")
print(str1 + str2)

answer = input("Do you like GOA? yes/no")
if answer == "yes":
    name2 = input("What's your name again i forgot?")
    print("Goodbye " + name2)
else:
    print("Goodbye")


letter = input("Enter a letter: ")
if letter == "A":
    print("100")
if letter == 'B':
    print("80")
if letter == 'C':
    print("60")
if letter == 'F':
    print("Failed!!")


sentence1 = input("Which city do you live in?")
sentence2 = input("Which city were you born in?")
print(sentence1 == sentence2)