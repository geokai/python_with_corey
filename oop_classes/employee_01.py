"""A sample class to create an Employee object and class methods."""

# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 19/08/2017
# Author: George Kaimakis - https://github.com/geokai


import requests


class Employee:
    """A sample Employee class """

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        """create an employee object with first & last name and pay"""
        self.first = first.title()
        self.last = last.title()
        self.pay = pay

    @property
    def email(self):
        """returns an email from the name variables"""
        return '{}.{}@email.com'.format(self.first.lower()[0], self.last.lower())

    @property
    def full_name(self):
        """returns a cat of 'first' & 'last' variables"""
        return '{} {}'.format(self.first.title(), self.last.title())

    def apply_raise(self):
        """multiplies the instance 'pay' by a percentage"""
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        """retreives a monthly schedule form a url/web page"""
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        return 'Bad Response!'
