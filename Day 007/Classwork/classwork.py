# for i in iter(int, 1):
#     print("this loops forever") # Comment so it doesn't loop forever
name = input("Enter your name: ")
for i in range(10):
    print(name)
print()
for i in range(2): # this is the loop's head
    print("Hello World") # this is the loop's body
print()
for i in range(10000000000000): # this has a big number so it will be like infinity
    number = int(input("Enter a number "))
    if number > 100:
        print("Correct!")
        break
count = 0
names = ''
for count in range(5): # this loop will run 5 times to collect all 5 names
    names = names + input("Enter name: ") + ', '
    count += 1 
print(names)