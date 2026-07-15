class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance     

    def get_balance(self):              # getter() - reads private data
        return self.__balance

    def deposit(self,amount):           # setter() - write / update / validate data
        self.__balance += amount

obj = BankAccount("Prachi",500)

print("ur balance is:", obj.get_balance())
obj.deposit(2000)
print("balance after deposit is:", obj.get_balance())