"""A class to create an Employee object with class variables
and class methods.
"""

# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 14/08/17
# Author: George Kaimakis - https://github.com/geokai


class Employee:
    """Creates an employee in terms of first & last names, pay amount
    and email address
    """

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
        """sets the class variable, raise_amt to a value"""
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """An alt init to handle an input in string format to create
        a new employee
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """determines if a day of the week is a work day"""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
