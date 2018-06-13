from employee import Employee
from manager import Manager
from developer import Developer
import datetime

# =============================================================================
# Employee Class Example
# =============================================================================
print('\n')
print('-' * 100)
print('Employee Class Example')
print('-' * 100)
print('\n')

# Instantiating Instances
emp_1 = Employee('Jane', 'Doe', 30000)

# Using Alternate Constructor to Instantiate Instances
emp_2_str = 'John-Doe-20000'
emp_2 = Employee.from_string(emp_2_str)

print('---------- Employee 1 ----------')
print(emp_1.full_name)
print(emp_1.email)
print('Employee 1 Pay: ', emp_1.pay)
print('Employee 1 Raise Amount: ', emp_1.raise_amount)
emp_1.apply_raise()
print('Employee 1 New Pay: ', emp_1.pay)
print('\n')

print('---------- Employee 2 ----------')
print(emp_2.first)
emp_2.full_name = 'Steve French'
print(emp_2.full_name)
print(emp_2.email)
del emp_2.full_name
print('Full name is now: ', emp_2.full_name)
print('Employee 2 Pay: ', emp_2.pay)
print('Employee 2 Raise Amount: ', emp_2.raise_amount)
emp_2.set_raise_amount(1.10)
print('Employee 2 New Raise Amount: ', emp_2.raise_amount)
emp_2.apply_raise()
print('Employee 2 New Pay: ', emp_2.pay)
print('\n')

print('Number of Employees Created: ', Employee.num_of_employees)

# =============================================================================
# Developer Sub Class Example
# =============================================================================
print('\n')
print('-' * 100)
print('Developer Sub Class Example')
print('-' * 100)
print('\n')

# Instantiating instances
dev_1 = Developer('Arin', 'Blue', 40000, 'Python')

print('---------- Developer 1 ----------')
print(dev_1.full_name)
print(dev_1.email)
print('Developer 1 Pay: ', dev_1.pay)
print('Developer 1 Raise Amount: ', dev_1.raise_amount)
dev_1.apply_raise()
print('Developer 1 New Pay: ', dev_1.pay)

# =============================================================================
# Manager Sub Class Example
# =============================================================================
print('\n')
print('-' * 100)
print('Manager Sub Class Example')
print('-' * 100)
print('\n')

# Instantiating instances
mgr_1 = Manager('Sue', 'Smith', 80000, [dev_1])

# mgr_1 = Manager('Sue', 'Smith', 80000, [dev_1, emp_2])

print('---------- Manager 1 ----------')
print(mgr_1.full_name)
print(mgr_1.email)
print('Manager 1 Pay: ', mgr_1.pay)
print('Manager 1 Raise Amount: ', mgr_1.raise_amount)
mgr_1.apply_raise()
print('Manager 1 New Pay: ', mgr_1.pay)

# Adding employees to list and printing them
print('\n')
print('Employees this manager supervises:')
mgr_1.add_employee(emp_1)
mgr_1.add_employee(emp_2)
mgr_1.print_employees()

# =============================================================================
# Date Time Example
# =============================================================================
print('\n')
print('-' * 100)
print('Date Time Example')
print('-' * 100)
print('\n')

# Create date objects
# (Year-Month-Day)
# Friday
my_date = datetime.date(2018, 6, 8)
# Saturday
my_other_date = datetime.date(2018, 6, 9)

print('Is this day (Friday) a workday? ', Employee.is_workday(my_date))
print('Is this day (Saturday) a workday? ', Employee.is_workday(my_other_date))

# =============================================================================
# Helpful Tips
# =============================================================================

print('\n')
# Test if main has run
# if __name__ == '__main__':
#     print('I executed!')

# Output Info -----------------------------------------------------------------

# Output class or instance info
# print(emp_1.__dict__)
# print(Employee.__dict__)

# Output class or instance info
# print(help(Employee))

# Output useful info to other devs or user(s) - See employee.py for more info
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# Type Checking ---------------------------------------------------------------
# Not good practice to use this. There are some exceptions to this rule

# Check if an object is an instance of a class
# print('Is Manager an instance of Manager Class?')
# print(isinstance(mgr_1, Manager))
# print('Is Manager an instance of Employee Class?')
# print(isinstance(mgr_1, Employee))
# print('Is Manager an instance of Developer Class?')
# print(isinstance(mgr_1, Developer))

# Check if a class is a subclass of another class
# print('Is Developer Class a subclass of Employee Class?')
# print(issubclass(Developer, Employee))
# print('Is Manager Class a subclass of Employee Class?')
# print(issubclass(Manager, Employee))
# print('Is Manager Class a subclass of Developer Class?')
# print(issubclass(Manager, Developer))

# Check the type of an object
# print('This object is of type: ', type(emp_1.pay))

# Helper Operators and Functions ----------------------------------------------

# Arithmetic Operators
# Addition:         +
# Subtraction:      -
# Multiplication:   *
# Division:         /       # Python 2 truncates decimals but Python 3 does not
# Floor Division:   //      # Truncates decimals on division
# Exponent:         **      # 3 ** 2 (3 squared = 9) (3 to the power of 2 = 9)
# Modulus:          %       # Returns the remainder after a division

# Arithmetic functions
# Absolute Value:   abs()   # Returns the absolute value of what's passed in
# ------------------------- # eg. abs(-3) = 3
# Round a Value:    round() # Returns the rounded value of what's passed in
# ------------------------- # You can also pass in how many decimal places to
# ------------------------- # round to as a second parameter

# Check the length of a list
# print(len(mgr_1.employees))
