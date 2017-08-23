"""This is the user interface script to the 'oop.py' employee class file"""


from oop_05 import Employee



emp_1 = Employee('george', 'kaimakis', 50000)
emp_2 = Employee('TEST', 'EMPLOYEE', 60000)

# # this is equivalent to __str__ and str():
# print(emp_1)

# These pairs are equivalent - this is for the official object representation:
# print(repr(emp_1))
# print(emp_1.__repr__())

# These pairs are equivalent - this is for the informal object representation:
print(str(emp_1))
print(emp_1.__str__())

# this uses the special method __add__ on the pay instance variable:
# print(emp_1 + emp_2)

# this uses the special method __len__ to count the characters of full_name:
# print(len(emp_1))

# These pairs are equivalent - behind the scenes stuff:
# print(1+2)
# print(int.__add__(1, 2))

# print('a'+'b')
# print(str.__add__('a', 'b'))
