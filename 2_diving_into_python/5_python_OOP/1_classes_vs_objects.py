# An object represent any real world thing
# Objects are often characterised by their properties(attributes) and methods(3_functions)
# The object's attributes describes the features that the object can have while methods are the
# functionalities associated with the object

# Objects are also associated with classes
# The necessity of a class comes in especially where we have many objects.
# Thus, an object is simply an instance of a class

#  Creating a class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age                         # Instance attributes
        self.gender = gender

    def person_interest(self, pet):
        return f"I love my {pet}"


#     creating instances/ objects of the person class
person1 = Person("Erick", 21, "Male")
first_name = person1.name
my_age = person1.age
gender1 = person1.gender
interest = person1.person_interest("dog")
print(interest)


class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.year},{self.color}, {self.model}")

    def stop(self):
        print(f"You drive the {self.year},{self.color}, {self.model}")


car1 = Car("BMW", 2024, "Black", True)
car2 = Car("Corvette", 2025, "White", False)
car1.drive()
car2.stop()

# Since classes usually take up alot of space, it is advisable to put the classes in a separate
# python file. The separate python file is then imported as a module.

# ***************** CLASS ATTRIBUTES ************************
# These are attributes created within the class but outside the constructor. These attributes are
# common to all the abjects of the class. As a good practice, the class attribute should be
# accessed via the class name rather than the object instances


class Student:
    department = "Computer Science"

    def __init__(self, name, reg_no, course):
        self.name = name
        self.reg_no = reg_no
        self.course = course

    def stu_details(self):
        print(f"My name is {self.name} of registration no {self.reg_no}.")
        print(f"I am from the department of {Student.department}, taking {self.course} as a "
              f"course.")


student1 = Student("Erick Ondiwa", "CCS/00072/021", "Computer Science")
student1.stu_details()
print(student1.name)
print(Student.department)




