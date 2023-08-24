# Feature: Encapsulation restricts the access to certain attributes and methods, protecting them from unauthorized access.

# Example:

class BankAccount:
    def __init__(self):
        self.balance = 0
        self._pin = 1234  # Protected attribute
        self.__account_number = "1234567890"  # Private attribute

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.__account_number

# Creating an object
account = BankAccount()

# Accessing attributes and methods
account.deposit(1000)
print(account.get_balance())          # Output: 1000
print(account.get_account_number())   # Output: 1234567890