"""This is the user interface script to the 'oop.py' employee class file"""


from oop_04 import Developer, Manager



dev_1 = Developer('george', 'kaimakis', 50000, 'Python')
dev_2 = Developer('TEST', 'EMPLOYEE', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# print(dev_1.full_name())
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
