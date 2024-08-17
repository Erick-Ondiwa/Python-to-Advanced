# An object represent any real world thing
# Objects are often characterised by their properties(attributes) and methods(functions)
# The object's attributes describes the features that the object can have while methods are the functionalities
# associated with the object

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
gender1 = person1.name
interest = person1.person_interest("dog")
print(interest)
