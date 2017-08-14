# Python Object-Oriented Programming:


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """create an emplayee object with the following variables"""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def full_name(self):
        """returns a cat of 'first' & 'last' variables"""
        return '{} {}'.format(emp_1.first, emp_1.last)

    def apply_raise(self):
        """multiplies the instance 'pay' by a percentage"""
        self.pay = int(self.pay * raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('George', 'Kaimakis', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.__dict__)

# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05

# print(emp_1.__dict__)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)
