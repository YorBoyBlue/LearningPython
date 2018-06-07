from employee import Employee
from manager import Manager
from developer import Developer
import datetime

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
print(emp_1.get_full_name())
print(emp_1.email)
print('Employee 1 Pay: ', emp_1.pay)
print('Employee 1 Raise Amount: ', emp_1.raise_amount)
emp_1.apply_raise()
print('Employee 1 New Pay: ', emp_1.pay)
print('\n')


print('---------- Employee 2 ----------')
print(emp_2.get_full_name())
print(emp_2.email)
print('Employee 2 Pay: ', emp_2.pay)
print('Employee 2 Raise Amount: ', emp_2.raise_amount)
emp_2.set_raise_amount(1.10)
print('Employee 2 New Raise Amount: ', emp_2.raise_amount)
emp_2.apply_raise()
print('Employee 2 New Pay: ', emp_2.pay)
print('\n')

print('Number of Employees Created: ', Employee.num_of_employees)

# =============================================================================
print('\n')
print('-' * 100)
print('Developer Sub Class Example')
print('-' * 100)
print('\n')

# Instantiating instances
dev_1 = Developer('Arin', 'Blue', 40000, 'Python')

print('---------- Developer 1 ----------')
print(dev_1.get_full_name())
print(dev_1.email)
print('Developer 1 Pay: ',dev_1.pay)
print('Developer 1 Raise Amount: ', dev_1.raise_amount)
dev_1.apply_raise()
print('Developer 1 New Pay: ', dev_1.pay)
print('\n')


# =============================================================================
print('\n')
print('-' * 100)
print('Manager Sub Class Example')
print('-' * 100)
print('\n')

# Instantiating instances
man_1 = Manager('Some', 'Manager', 80000, dev_1)

print('---------- Manager 1 ----------')
print(man_1.get_full_name())
print(man_1.email)
print('Manager 1 Pay: ', man_1.pay)
print('Manager 1 Raise Amount: ', man_1.raise_amount)
man_1.apply_raise()
print('Manager 1 New Pay: ', man_1.pay)
print('\n')


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


# Helpful Tips ----------------------------------------------------------------

# Test if main has run
# if __name__ == '__main__':
#     print('I executed!')

# Output class or instance info
# print(emp_1.__dict__)
# print(Employee.__dict__)

# Output class or instance info
# print(help(Employee))
