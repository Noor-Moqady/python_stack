class BankAccount:
    def __init__(self, int_rate=0.01, account_balance=0):
        self.int_rate = int_rate
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self

    def display_account_info(self):
        print(f"Balance: ${self.account_balance}, Interest rate: {self.int_rate * 100}%")
        return self


class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = BankAccount()

    def display_user_balance(self):
        print(f"User name: {self.name}, User email: {self.email}")
        self.account_balance.display_account_info()
        return self

# Create user instances
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
noor = User("Noor Python", "noor@python.com")

# Perform operations and display account information
guido.account_balance.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(50).transfer_money(monty.account_balance, 100).display_user_balance()
monty.account_balance.make_deposit(50).make_deposit(500).make_withdrawal(100).display_user_balance()
noor.account_balance.make_deposit(500).make_withdrawal(50).make_withdrawal(20).make_withdrawal(150).display_user_balance()
