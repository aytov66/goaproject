for i in range(100):
    print(i + 1)
    i += 1
if i % 2 == 0:
    print("this number is even")
if i % 2 != 0:
    print("this number is odd")
i = 0
print()



number = int(input("Enter a number: "))
if number % 2 == 0:
    print("this number is even")
if number % 2 != 0:
    print("this number is odd")

print()


num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
if num2 > num1:
    print("მეტია")
elif num2 < num1:
    print("ნაკლებია")




firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
firstnumber += 1
secondnumber += 1
if firstnumber > secondnumber:
    print(firstnumber)
elif firstnumber < secondnumber:
    print(secondnumber)
