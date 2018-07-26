"""This is the user interface script to the 'oop.py' employee class file"""


from oop_04 import Employee, Developer, Manager



dev_1 = Developer('george', 'kaimakis', 50000, 'Python')
dev_2 = Developer('TEST', 'EMPLOYEE', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


# use of 'isinstance' and 'issubclass' functions:
print(isinstance(mgr_1, Manager))       # True
print(isinstance(mgr_1, Developer))     # False
print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Developer))   # False


# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.full_name())
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
