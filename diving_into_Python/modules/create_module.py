# Creating a module is just creating any other python file
# This module contains two functions which are to be reused in other files if necessary
def happy_birthday(name, age):
    print("Happy birthday "+name+",")
    print("Happy birthday dear "+name + ",")
    print("You are "+str(age)+" years old"+".")


def compute_sum(x, y):
    return x + y
