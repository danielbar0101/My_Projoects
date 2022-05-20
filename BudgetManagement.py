class Account:

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


acct1 = Account('Yossi', 18, 'Artist')

print(acct1.name)
print(acct1.job)

