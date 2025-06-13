x = 5      # int
y = 2.0    # float
z = x + y  # x is implicitly converted to float, result is float 7.0

x = "123"       # string
y = int(x)      # explicitly converting string to int
print(y + 1)    # outputs 124

x = int(input("Enter a number: "))
for i in range(1, x + 1):
    print(i)

x = 0
x = int(input("Enter a number: "))
i = 1
while i <= x:
    print(i)
    i += 1