import unittest
from employee import Employee

"""
Module for testing the give_raise() method
"""

class TestEmployee(unittest.TestCase):
    """
    Test class for testing the Employee class
    """

    def setUp(self):
        """creates Employee instance to use for testing"""
        first_name = "nikhil"
        last_name = "kapoor"
        ann_salary = 30_000
        self.my_employee = Employee(first_name, last_name, ann_salary)
    

    def test_give_default_raise(self):
        """Tests give_raise() with the default additional salary"""
        old_salary = self.my_employee.ann_salary
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.ann_salary, (old_salary + 50_000))
    

    def test_give_custom_salary(self):
        """Tests give_raise() with a custom salary"""
        old_salary = self.my_employee.ann_salary
        self.my_employee.give_raise(100_000)
        self.assertEqual(self.my_employee.ann_salary, (old_salary + 100_000))


if __name__ == "__main__":
    unittest.main()