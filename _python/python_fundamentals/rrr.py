class BankAccount:
    def __init__(self, int_rate=0.01, account_balance=0):
        self.interest_rate = int_rate
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee and deduct $5")
            self.account_balance -= 5
        return self

    def transfer_money(self, other_account, amount):
        self.make_withdrawal(amount)
        other_account.make_deposit(amount)
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance * self.interest_rate
        return self

    def display_account_balance(self):
        print(f"Balance: ${self.account_balance}, Interest rate: {self.interest_rate}")
        return self


class User:
    def __init(self, name, email_address):
        self.name = name
        self.email = email_address
        self.accounts = []

    def create_account(self, int_rate=0.01, account_balance=0):
        new_account = BankAccount(int_rate, account_balance)
        self.accounts.append(new_account)
        return self

    def make_deposit(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].make_deposit(amount)
        else:
            print("Invalid account index")

    def make_withdrawal(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].make_withdrawal(amount)
        else:
            print("Invalid account index")

    def transfer_money(self, account_index_from, other_user, account_index_to, amount):
        if 0 <= account_index_from < len(self.accounts) and 0 <= account_index_to < len(other_user.accounts):
            self.accounts[account_index_from].transfer_money(other_user.accounts[account_index_to], amount)
        else:
            print("Invalid account index")

    def yield_interest(self, account_index):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].yield_interest()
        else:
            print("Invalid account index")

    def display_user_accounts(self):
        print(f"User name: {self.name}, User email: {self.email}")
        for i, account in enumerate(self.accounts):
            print(f"Account {i}:")
            account.display_account_balance()


# Create User instances
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
noor = User("Noor Python", "noor@python.com")

# Create accounts for users
guido.create_account(0.01, 1000)
monty.create_account(0.02, 500)
noor.create_account(0.015, 1500)

# Perform transactions
guido.make_deposit(0, 100).make_withdrawal(0, 50).transfer_money(0, monty, 0, 100).yield_interest(0)
monty.make_deposit(0, 50).make_withdrawal(0, 100).yield_interest(0)
noor.make_deposit(0, 500).make_withdrawal(0, 50).transfer_money(0, monty, 0, 200).yield_interest(0)

# Display user account balances
guido.display_user_accounts()
monty.display_user_accounts()
noor.display_user_accounts()
