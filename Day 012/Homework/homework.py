# Task 1: Blood Pressure Analysis
systolic = int(input("Enter systolic pressure: "))
diastolic = int(input("Enter diastolic pressure: "))

if systolic > 140 or diastolic > 90:
    print("High blood pressure")
elif systolic < 90 or diastolic < 60:
    print("Low blood pressure")
else:
    print("Normal blood pressure")

# Task 2: Weight Check by Age
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age < 10:
    if weight < 20:
        print("Low weight")
    elif weight <= 40:
        print("Normal weight")
    else:
        print("High weight")
elif age <= 17:
    if weight < 40:
        print("Low weight")
    elif weight <= 65:
        print("Normal weight")
    else:
        print("High weight")
else:
    if weight < 50:
        print("Low weight")
    elif weight <= 90:
        print("Normal weight")
    else:
        print("High weight")

# Task 3: Age and Time Suggestion
age = int(input("Enter your age: "))
hour = int(input("Enter the hour (0-23): "))

if age < 18 and hour >= 22:
    print("Time to sleep")
elif age >= 60 and hour >= 21:
    print("Rest is recommended")
else:
    print("You can keep going")

# Task 4: Physical Activity Suggestion
age = int(input("Enter your age: "))
heart_rate = int(input("Enter your heart rate: "))

if age < 30 and heart_rate < 140:
    print("You can exercise more")
elif age >= 30 and heart_rate > 170:
    print("You need rest")
else:
    print("Activity level is normal")

# Task 5: Food Recommendation by Age
age = int(input("Enter your age: "))

if age <= 12:
    print("Eat foods with lots of vitamins")
elif age <= 25:
    print("Eat energy-giving foods")
elif age <= 59:
    print("Eat a balanced diet")
else:
    print("Eat low-calorie and light foods")
