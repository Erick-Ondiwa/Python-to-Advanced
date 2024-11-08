# A static method is a method that belong to a class rather than any object (instance) of that
# class
# A static method is different from either the instance or class methods since it does not take
# any default parameter.
# They are also bound to the class, not the object, and cannot access or modify the class state
# They are used to create utility 4_functions that perform a task in isolation.
# Static methods are defined using the @staticmethod decorator.

class Employee:

    def __init__(self, name, job_position):
        self.name = name
        self.job_position = job_position

    def get_info(self):
        print(f"{self.name} - {self.job_position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]

        return position in valid_positions


employee1 = Employee(name="Erick", job_position="Manager")
employee1.get_info()
check_position = Employee.is_valid_position(position="Janitor")
print(check_position)
