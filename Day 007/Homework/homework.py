for i in range(10):
    print(i + 1)
    i += 1
print()
for i in range(5):
    print("Hello World")
    i += 1
print()
for i in range(0, 10, 2):  # if we want the 10 to be included, we can do range(0, 12, 2)
    print(i)
    i += 2
# a for loop repeats selected code a certain amount of times using a range (start, stop ,step)