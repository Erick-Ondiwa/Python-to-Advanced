import create_module as module1
module1.happy_birthday("Erick", 21)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = module1.compute_sum(num1, num2)
print(total)

# Other ways of using 3_modules
# 1.
# This will only import the specified 4_functions||classes||variables||constants
from create_module import happy_birthday, compute_sum
happy_birthday("Shadrack", 18)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

total_sum = compute_sum(x, y)
