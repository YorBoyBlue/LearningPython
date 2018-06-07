from employee import Employee


class Manager(Employee):

    raise_amount = 1.5

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('--->', employee.get_full_name())
