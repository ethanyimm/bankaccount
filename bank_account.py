import uuid
import logging

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.account_number = uuid.uuid4()
        self.balance = initial_amount
        self.name = account_name
        self.transaction_history = []
        logging.info(f"Account {self.account_number} created. Initial balance = ${self.balance:.2f}")

    def log_transaction(self, transaction_type, amount):
        self.transaction_history.append({"type": transaction_type, "amount": amount})
        logging.info(f"Transaction: {transaction_type} - Amount: ${amount:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        self.log_transaction("Deposit", amount)
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            self.log_transaction("Withdrawal", amount)
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n*********\n\nBeginning Transfer...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        self.log_transaction("Deposit with Interest", amount)
        print("\nDeposit complete.")
        self.get_balance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            self.log_transaction("Withdrawal with Fee", amount + self.fee)
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")