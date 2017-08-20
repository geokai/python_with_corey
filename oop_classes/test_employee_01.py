"""Unit_test script for 'employee_01.Employee' class"""

import unittest
from unittest.mock import patch
from employee_01 import Employee


# Python Object-Oriented Programming by Corey Schafer:
# https://youtube.com/user/schafer5/playlist

# This file was created on 19/08/2017
# Author: George Kaimakis - https://github.com/geokai


class TestEmployee(unittest.TestCase):
    """Test class for Employee class - the print statement at each
    method is for debug purposes only
    """
    @classmethod
    def setUpClass(cls):
        """run the following code before the first test"""
        # print('setUpClass\n')

    @classmethod
    def tearDownClass(cls):
        """run the following code after the last test"""
        # print('tearDownClass')

    def setUp(self):
        """run the following code before each test"""
        # print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)    # note case:
        self.emp_2 = Employee('sue', 'SMITH', 60000)

    def tearDown(self):
        """run the following code after each test"""
        # print('tearDown\n')

    def test_email(self):
        """test that the email address is correctly formed"""
        # print('test_email')

        self.assertEqual(self.emp_1.email, 'c.schafer@email.com')
        self.assertEqual(self.emp_2.email, 's.smith@email.com')

        self.emp_1.first = 'john'   # note case:
        self.emp_2.first = 'JANE'

        self.assertEqual(self.emp_1.email, 'j.schafer@email.com')
        self.assertEqual(self.emp_2.email, 'j.smith@email.com')

    def test_full_name(self):
        """test that the full name is correctly formed"""
        # print('test_full_name')

        self.assertEqual(self.emp_1.full_name, 'Corey Schafer')
        self.assertEqual(self.emp_2.full_name, 'Sue Smith')

        self.emp_1.first = 'JOHN'   # note case:
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.full_name, 'John Schafer')
        self.assertEqual(self.emp_2.full_name, 'Jane Smith')

    def test_apply_raise(self):
        """test that the pay raise method works correctly"""
        # print('test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """test the url request using mocking"""
        with patch('employee_01.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')


            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
