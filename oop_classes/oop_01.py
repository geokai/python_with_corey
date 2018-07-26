# Python Object-Oriented Programming:


class Employee:

    def __init__(self, first, last, pay):
        """create an emplayee object with the following variables"""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        """returns a cat of 'first' & 'last' variables"""
        return '{} {}'.format(emp_1.first, emp_1.last)


emp_1 = Employee('George', 'Kaimakis', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# these two lines of code do exactly the same - the first is converted
# to the second behind the scenes.
print(emp_1.full_name())
print(Employee.full_name(emp_1))
