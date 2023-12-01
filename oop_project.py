from bank_account import BankAccount, InterestRewardsAcct, SavingAcct

def main():
    # Create a BankAccount instance
    initial_amount = float(input("Enter initial amount for BankAccount: "))
    account_name = input("Enter account name for BankAccount: ")
    account = BankAccount(initial_amount, account_name)

    # Demonstrate BankAccount methods
    account.get_balance()

    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)

    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)

    # Create an InterestRewardsAcct instance
    interest_account = InterestRewardsAcct(1000, "InterestAccount")

    # Demonstrate InterestRewardsAcct methods
    interest_account.get_balance()

    interest_deposit_amount = float(input("Enter amount to deposit into InterestAccount: "))
    interest_account.deposit(interest_deposit_amount)

    # Create a SavingAcct instance
    saving_account = SavingAcct(1500, "SavingAccount")

    # Demonstrate SavingAcct methods
    saving_account.get_balance()

    saving_deposit_amount = float(input("Enter amount to deposit into SavingAccount: "))
    saving_account.deposit(saving_deposit_amount)

if __name__ == "__main__":
    main()