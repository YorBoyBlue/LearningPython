class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@veroot.com'

    def get_full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay *= self.raise_amount
