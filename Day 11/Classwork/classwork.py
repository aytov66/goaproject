a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
c = int(input('Please enter the third number: '))
print(a + b + c)
print()



for i in range(1, 100, 2):
    print(i)

print()

for i in range(1, 101):
    if i % 3 == 0:
        print(i)
print()


total = 0
for i in range(1, 101):
    total += i

print("The sum is:", total)