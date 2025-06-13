numbers = list(range(160, 171)) 
heartbeat = int(input('What is your heartbeat right now?'))
if heartbeat >= 180:
    print('Your heartbeat is too high, Take a chill pill ;D')
elif heartbeat in numbers:
    print('Your heartbeat is normal, You are healthy')
elif heartbeat <= 160:
    print('Your heartbeat is too low, Try exercising and hydrating ')
print()

ages = list(range(13, 20))
ages2 = list(range(20, 60))
age = int(input('What is your age? '))
if age < 0:
    print('Wrong age')
elif age < 13:
    print('Kid')
elif age in ages:
    print('Teenager')
elif age in ages2:
    print('Adult')
else:
    print('Retired')
