class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + '.' + last + '@veroot.com'

        # Update a value for class and all instances
        Employee.num_of_employees += 1

    def get_full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Methods
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        first, last, pay = employee_str.split('-')
        return cls(first, last, pay)

    # Static Methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
