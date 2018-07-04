import sqlite3
from employee import Employee

# In memory DB example
# conn = sqlite3.connect(':memory:')

# In file DB example
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# Create a table with fields and types for the fields =========================

# c.execute("""CREATE TABLE employees (
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   first VARCHAR(20),
#                   last VARCHAR(20),
#                   pay INTEGER
#               )""")
# conn.commit()
#
# # Insert data into the created table and fields =============================

# c.execute(
#     "INSERT INTO employees(first, last, pay) VALUES ('Arin', 'Blue', 40000)")
# conn.commit()
# c.execute(
#     "INSERT INTO employees(first, last, pay) VALUES ('Jane', 'Doe', 70000)")
# conn.commit()

# Inserting multiple entries at once ==========================================

# data_person_name = [('Michael', 'Fox', 40000),
#                     ('Adam', 'Miller', 90000),
#                     ('Andrew', 'Peck', 20000),
#                     ('James', 'Shroyer', 70000),
#                     ('Eric', 'Burger', 50000)]
#
# c.executemany('INSERT INTO employees(first, last, pay) VALUES (?,?,?)',
#               data_person_name)
# conn.commit()

# Using classes ===============================================================

emp_1 = Employee('Steve', 'Jobs', 100000000)
emp_2 = Employee('Steven', 'Hawking', 1000000000)


# Use class directly
# c.execute('INSERT INTO employees(first, last, pay) VALUES (?,?,?)',
#           (emp_1.first, emp_1.last, emp_1.pay))
# Use Dictionary of classes values
# c.execute('INSERT INTO employees(first, last, pay) VALUES (:first,:last,:pay)',
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()

def insert_emp(emp):
    with conn:
        c.execute(
            'INSERT INTO employees(first, last, pay) VALUES '
            '(:first,:last,:pay)',
            {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """ UPDATE employees SET pay = :pay WHERE first = :first AND 
                last = :last""",
            {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last",
            {'first': emp.first, 'last': emp.last})


# remove_emp(emp_1)
# remove_emp(emp_2)
# insert_emp(emp_1)
# insert_emp(emp_2)

emps = get_emp_by_name('Jobs')
print(emps)

update_pay(emp_1, 200000000)
emps = get_emp_by_name('Jobs')
print(emps)

# Selecting data from the DB ==================================================

c.execute(
    "SELECT * FROM employees WHERE (last='Blue' OR last='Doe' OR "
    "last='Hawking')")
# Returns the next row in the results and if there is nothing it returns none
# result = c.fetchone()
# Returns the specified amount of rows from the result as a list
# result = c.fetchmany(5)
# Returns all rows from result as a list
result = c.fetchall()
print(result)

# Close the connection ========================================================

conn.close()
