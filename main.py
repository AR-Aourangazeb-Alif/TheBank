"""
1. Savings account:
    -  Earns monthly/quarterly interest

    -  Minimum balance requirement (e.g., $100)

    -  Limited withdrawals per month (e.g., 2)

2. Checking account:
    -  No interest (or low interest)

    -  Unlimited withdrawals/transactions

    -  Basically a normal bank account

3. Students account:
    -  Lower minimum balance

    -  Age restriction (e.g., <25 years)

    -  Example: 5 to 10 free withdrawals per month.

    -  Charges a small fee for exceeding the limit.
4. Certificate of Deposit (CD):
    -  Fixed term (e.g., 6 months, 1 year)

    -  Higher interest rates (10%)

    -  Penalty for early withdrawal (charge fees)

    -  Automatic renewal option 

"""

from bank_account import BankAccount
from instantiate_csv import instantiate_from_csv

instantiate_from_csv()


BankAccount.listAccounts()

print(BankAccount.all)