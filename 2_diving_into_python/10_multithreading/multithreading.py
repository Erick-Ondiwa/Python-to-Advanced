import threading
import time


def compute_area(length, width):
    time.sleep(4)
    return length * width


def compute_perimeter(length, width):
    time.sleep(2)
    return 2 * (length + width)


task1 = threading.Thread(target=compute_area, args=(10, 6))
task2 = threading.Thread(target=compute_perimeter, args=(10, 6))
print(f"The area is {task1}")
print(f"The perimeter is {task2}")
