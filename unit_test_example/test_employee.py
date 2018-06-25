import unittest
from unittest.mock import patch
from learning_python.employee import Employee


class TestEmployee(unittest.TestCase):

    # This runs at the beginning of executing this entire class
    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass\n')
        # Could be used to query from a database once for the whole file.
        # You would use the tearDownClass method to tear it down when done

    # This runs after every test has finished executing in this class
    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    # Called at the beginning of each test
    def setUp(self):
        print('\nsetUp')
        self.emp_1 = Employee('John', 'Doe', 50000)
        self.emp_2 = Employee('Jane', 'Doe', 60000)

    # Called at the end of every test
    def tearDown(self):
        print('tearDown')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'John.Doe@veroot.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@veroot.com')

        self.emp_1.first = 'Test'
        self.emp_2.first = 'Test'

        self.assertEqual(self.emp_1.email, 'Test.Doe@veroot.com')
        self.assertEqual(self.emp_2.email, 'Test.Doe@veroot.com')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.emp_1.full_name, 'John Doe')
        self.assertEqual(self.emp_2.full_name, 'Jane Doe')

        self.emp_1.first = 'Test'
        self.emp_2.first = 'Test'

        self.assertEqual(self.emp_1.full_name, 'Test Doe')
        self.assertEqual(self.emp_2.full_name, 'Test Doe')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success!')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
