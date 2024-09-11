# Class methods are methods that are bound to the class itself rather than its object.
# They can modify the class state that applies across all instances of the class.
# To define a class method, you use the @classmethod decorator, and it takes cls as the first
# parameter.
# The cls parameter points to the class, not the object instance.
# Class methods can access and modify class variables but not instance variable

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name} - {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students is: {cls.count}"


student1 = Student(name="Erick", gpa=69)
student2 = Student(name="Shadrack", gpa=66)

# print(student1.get_count())
print(Student.get_count())
