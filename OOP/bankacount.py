class bankacount:
    def __init__ (self,owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Insufficient funds.")


s1 = bankacount("Ali", 1000)
s1.deposit(500)
s1.withdraw(200)
