"""A class to create an Employee object with class variables
and class methods.
"""

# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 23/08/17
# Author: George Kaimakis - https://github.com/geokai


class Employee:
    """Creates an employee in terms of first & last names, pay amount
    and email address
    """

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        """create an emplayee object in terms of a first and last name,
        a pay amount and an email address.
        """
        self.first = first.title()
        self.last = last.title()
        self.email = first[0].lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def full_name(self):
        """returns a cat of 'first' & 'last' variables"""
        return '{} {}'.format(self.first.title(), self.last.title())

    def apply_raise(self):
        """multiplies the instance 'pay' by a percentage"""
        self.pay = int(self.pay * self.raise_amt)


    def __repr__(self):
        """magic method __repr__"""
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        """magic method __str__"""
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        """adding the pay of two employees using a spacial method"""
        return self.pay + other.pay

    def __len__(self):
        """length of full name of employee uaing special method"""
        return len(self.full_name())
