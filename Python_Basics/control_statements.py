# A. Decision Making
# 1. if...and elseif statements
age: int = int(input("Enter Your age:"))
if not (age, int):
    print("Please enter a valid age")
elif age < 0 or age == 0:
    print("You're not yet born")
elif 0 < age < 18:
    print("You're still a child")
elif 18 <= age < 100:
    print("You're an adult")
else:
    print("You just hit a centuary. You're too  old")


# B. Control statements(Looping)
# 1.while...loop
name: str = ""
while len(name) == 0:
    name = input("Enter your name")
print("Your name is " + name)

# 2.for...loop
for seconds in range(50, 0, -2):
    print(seconds)

import time
for count in range(0, 60, 1):
    print(count)
    time.sleep(1)
print("One Minute")