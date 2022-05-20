class Account:

    currency = 'NIS'

    def __init__(self, name, age, job, balance):
        self.name = name
        self.age = age
        self.job = job
        self.balance = balance

    def income(self, amount_in):
            self.balance += amount_in

    def expense(self, amount_out):
        self.balance -= amount_out



acct1 = Account('Yossi', 18, 'Artist', 0)
print(acct1.name)
print(acct1.balance)

acct1.expense(300)
print(acct1.balance)
