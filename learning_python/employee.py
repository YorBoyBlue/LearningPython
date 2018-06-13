class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    # Constructor =============================================================
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)

        # Update a value for class and all instances
        Employee.num_of_employees += 1

    # Getters, Setters and Deleter ============================================

    # Property decorator allows a method to be called like a property.
    # ie. without the parenthesis
    # Works great when having to turn a property into a method and don't want
    # to have to change all the use cases to proper syntax
    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@veroot.com'.format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(' ')

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None
        print('Deleted Name!')

    # Regular Methods =========================================================
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Methods ===========================================================
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_str):
        first, last, pay = employee_str.split('-')
        return cls(first, last, pay)

    # Static Methods ==========================================================
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Helper Function Overrides ===============================================

    # Used to output information when printing an instance of a class
    # repr is meant to be an unambiguous representation of the object and
    # should be used to display info to developers (debugging, logging, etc.)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last,
                                                 self.pay)

    # Used to output information when printing an instance of a class
    # str is meant to be a more readable representation of the object and
    # should be used to display info to the end user.
    # If you define str it will be the default when using print on an instance
    # if not the repr will be the fallback
    # you can call each one directly as well. Example in main.py
    def __str__(self):
        return '{} - {}'.format(self.get_full_name(), self.email)
        # The line below can be used in a conditional to force it to fall back
        # to the default implementation. This is usually used if some condition
        # cannot be handled by your implementation and to check if the default
        # can handle it before throwing an error.
        # return NotImplemented
