# Functions - this is a section of reusable code that is only executed when called

#  program to compute the area volume of a cylinder

# A function to compute the cross-section area of a circle
def compute_circle_area(radius):
    PI = 3.142

    return PI * radius * radius
# Using the return value above to compute the volume of the cylinder
def compute_volume():
    HEIGHT: int = 40
    area = compute_circle_area(14)
    return area * HEIGHT


volume = compute_volume()
print(volume)
