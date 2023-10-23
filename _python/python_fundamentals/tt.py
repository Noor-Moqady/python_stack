class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate  # Annual interest rate (default: 1%)
        self.balance = balance  # Initial balance (default: 0)

    def deposit(self, amount):
        self.balance += amount
        return self  # Return the instance to allow method chaining

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds. Withdrawal not allowed.")
        return self  # Return the instance to allow method chaining

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.int_rate * 100}%")
        return self  # Return the instance to allow method chaining

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self  # Return the instance to allow method chaining

# Example usage of the BankAccount class
account1 = BankAccount()  # Creates an account with default values
account2 = BankAccount(0.02, 1000)  # Creates an account with a 2% interest rate and $1000 initial balance

# Perform operations and display account information
account1.deposit(500).deposit(200).withdraw(100).yield_interest().display_account_info()
account2.deposit(200).deposit(300).withdraw(50).withdraw(100).yield_interest().display_account_info()
