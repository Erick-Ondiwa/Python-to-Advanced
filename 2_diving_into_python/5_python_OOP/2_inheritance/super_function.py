# The super() function in Python is often used in the context of inheritance, where it enables a
# child class to access methods and properties of its parent class without directly referencing
# the parent. This is particularly helpful when you have overridden a method in a subclass but
# still want to call the parent class’s version of that method.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        # Base pay calculation for a regular employee
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # Initialize the parent class with the name and salary attributes
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        # Call the parent class's calculate_pay method and add the bonus
        base_pay = super().calculate_pay()
        return base_pay + self.bonus


# Example usage:
employee = Employee("Alice", 50000)
manager = Manager("Bob", 70000, 15000)

print(f"Employee Pay: {employee.calculate_pay()}")  # Output: 50000
print(f"Manager Pay: {manager.calculate_pay()}")  # Output: 85000

# Explanation of super() in This Context
# In the __init__ method of Manager:
# The super().__init__(name, salary) call is used to initialize name and salary attributes from
# the Employee class. This eliminates the need to directly call Employee.__init__(self, name,
# salary), making the code more maintainable.
# In the calculate_pay method of Manager:
# The super().calculate_pay() call invokes the calculate_pay method of the Employee class to get
# the base salary. This is then combined with the bonus specific to managers, allowing for an
# overridden version that incorporates the additional behavior.
