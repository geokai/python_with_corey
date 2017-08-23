"""This is the user interface script to the 'oop.py' employee class file"""


from employee_01 import Employee


EMPLOYEES = []

def list_employees():
    """print out a formatted list of employees"""
    print()
    for i, j in enumerate(EMPLOYEES, 1):
        print('Employee No: {}'.format(i))
        print('{}: '.format(j.full_name()))
        print('\tPay: {}'.format(j.pay))
        print('\temail: {}'.format(j.email))
        print('\tRaise Amount: {}'.format(j.raise_amt))
        print()

def main():
    """run the Employee class functionality"""
    emp_01 = Employee('GEORGE', 'kaimakis', 50000)
    EMPLOYEES.append(emp_01)
    emp_02 = Employee('Karen', 'Smiley', 55000)
    EMPLOYEES.append(emp_02)

    # Employee.raise_amt = 1.04
    # print('Raise Amount: {}'.format(Employee.raise_amt))
    # emp_01.apply_raise()
    # emp_02.apply_raise()

    list_employees()


if __name__ == '__main__':
    main()


# the following to be used with the 'from_string' method:
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-75000'
