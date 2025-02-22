from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self):
        self.account_type = "Checking Account"