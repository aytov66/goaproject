cars = ["BMW", "Mercedes", "Toyota", "Honda"]
cars[1], cars[2] = cars[2], cars[1]

print(cars)
# Indexing lets us access characters by position, but strings can't be changed this way
txt = "hello world, python html"
print(txt[0])
print(txt[-1])

#            0      1       2
example = ('one', 'two', 'three')
#           -1     -2      -3 
# This is how indexing works