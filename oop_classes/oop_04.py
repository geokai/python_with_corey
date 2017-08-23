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


class Developer(Employee):
    """Developer sub-class"""

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # Alt method to inherit
        self.prog_lang = prog_lang


class Manager(Employee):
    """Manager sub-class"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """adds an employee to the list of managed employees"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """removes an employee from the list of managed employees"""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """prints a list of managed employees"""
        for emp in self.employees:
            print('--->', emp.full_name())
