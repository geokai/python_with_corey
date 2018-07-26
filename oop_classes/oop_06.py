"""A class to create an Employee object with class variables
and class methods.
"""

# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 24/08/17
# Author: George Kaimakis - https://github.com/geokai


class Employee:
    """Creates an employee in terms of first & last names, pay amount
    and email address
    """

    def __init__(self, first, last):
        """create an emplayee object in terms of a first and last name,
        a pay amount and an email address.
        """
        self.first = first.title()
        self.last = last.title()

    @property
    def email(self):
        """getter for the email using the 'first' & 'last' variables"""
        return '{}.{}@email.com'.format(self.first[0].lower(), self.last.lower())

    @property
    def full_name(self):
        """getter for the full_name using 'first' & 'last' variables"""
        return '{} {}'.format(self.first.title(), self.last.title())

    @full_name.setter
    def full_name(self, name):
        """setter for full_name - to also set 'first' & 'last' variables"""
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        """deleter for full_name - to also delete 'first' & 'last' variables"""
        print('Delete name!')
        self.first = None
        self.last = None
