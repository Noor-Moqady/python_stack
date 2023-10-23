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
        if self.account_balance > amount2:
            self.account_balance -= amount2
        else:
            print("Insufficient funds: Charging a $5 fee and deduct $5")
        return self
    def transfer_money(self, other_user, amount3):
       self.make_withdrawal(amount3)
       other_user.make_deposit(amount3)
       return self
    def yield_interest(self):
        self.account_balance+(self.account_balance*self.intrest_rate)
        return self
    def display_user_balance(self):
        print(f"User name: {self.name}, User email: {self.email}, Balance: ${self.account_balance}, Interest rate: {self.intrest_rate}")
        return self
 
guido = BankAccount("Guido van Rossum", "guido@python.com")
monty = BankAccount("Monty Python", "monty@python.com")
noor = BankAccount("Noor Python", "noor@python.com", 0.2)

guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(50).transfer_money(monty, 100).display_user_balance().yield_interest()

monty.make_deposit(50).make_deposit(500).make_withdrawal(100).display_user_balance().yield_interest()

noor.make_deposit(500).make_withdrawal(50).make_withdrawal(20).make_withdrawal(150).display_user_balance().yield_interest()



