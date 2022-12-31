from datetime import date

today = date.today()


class Customer:
    """ A class representing a customer """

    def init(self, name, address, email=str, balance=0, debt_timer=today):
        self.name = name
        self.address = address
        self.balance = balance
        self.email = email
        self.debt_timer = debt_timer


bill = Customer("bill", "123 willow avenue")
print(bill.name)