class BankAccount:
    def __init__(self, name, email_adress, int_rate = 0.01, account_balance = 0):
        self.name = name
        self.email = email_adress
        self.intrest_rate = int_rate
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount2):
        self.account_balance -= amount2
        return self
    def transfer_money(self, other_user, amount3):
       self.make_withdrawal(amount3)
       other_user.make_deposit(amount3)
       return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        pass
    
guido = BankAccount("Guido van Rossum", "guido@python.com")
monty = BankAccount("Monty Python", "monty@python.com")
noor = BankAccount("Noor Python", "noor@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(50).transfer_money(monty, 500).display_user_balance()

monty.make_deposit(50).make_deposit(500).make_withdrawal(100).display_user_balance()

noor.make_deposit(500).make_withdrawal(50).make_withdrawal(20).make_withdrawal(150).display_user_balance()

print(guido.name)
print(monty.email)



