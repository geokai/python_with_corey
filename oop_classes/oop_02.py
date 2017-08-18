"""A class to create an Employee object with class variables
and class methods.
"""

# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 14/08/17
# Author: George Kaimakis - https://github.com/geokai



class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        """create an emplayee object in terms of a first and last name,
        a pay amount and an email address.
        """
        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first[0].lower() + '.' + last.lower() + '@company.com'
        # increments the class variable to keep track of number
        # of Employee objects created:
        Employee.num_of_emps += 1

    def full_name(self):
        """returns a cat of 'first' & 'last' variables"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """multiplies the instance 'pay' by a percentage"""
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(self, emp_str):
        pass


emp_1 = Employee('george', 'kaimakis', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("–" * 25)
print("Number of employees: " + str(Employee.num_of_emps))
print("–" * 25)

print()
# print(emp_1.__dict__)
# print("emp 1 pay: " + str(emp_1.pay))
# emp_1.apply_raise()
# print(emp_1.__dict__)
# print("emp 2 pay: " + str(emp_2.pay))
# print()

# print()
print("Employee raise amount: " + str(Employee.raise_amt) + "%")
print("emp_1 raise amount: " + str(emp_1.raise_amt))
print("emp_2 raise amount: " + str(emp_2.raise_amt))
print()

