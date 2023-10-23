class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} transferred ${amount} to {other_user.name}")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

# Create user instances
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
noor = User("Noor Python", "noor@python.com")

# Perform transactions
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(200)
guido.make_withdrawal(50)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(500)
monty.make_withdrawal(100)
monty.display_user_balance()

noor.make_deposit(500)
noor.make_withdrawal(50)
noor.make_withdrawal(20)
noor.make_withdrawal(150)
noor.display_user_balance()

# Transfer money from Guido to Monty
guido.transfer_money(monty, 300)

