class BankAccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print('невозможно снять деньги')
        else:
            self.__balance -= amount

    @property
    def get_balance(self):
        return self.__balance


a = BankAccount(1000, 'Tima')
print(a.get_balance())
a.withdraw(1200)
print(a.get_balance())
a.deposit(2000)
print(a.get_balance())
a.balance = 20000
print(a.get_balance())
