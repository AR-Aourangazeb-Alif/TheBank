from students_account import StudentsAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from cd import CD
from bank_account import BankAccount


def instantiate_from_csv():
    with open("accounts.csv", "r") as f:
        data = f.readlines()

    if len(data)>1:
        for i in range(1,len(data)):
            a = data[i].replace("\n","").split(",")
            (
            CheckingAccount(owner=(a[0].strip()), amount=(float(a[2].strip())), id=(int(a[1].strip()))) if a[-1] == "Checking Account" else 
            SavingsAccount(owner=(a[0].strip()), amount=(float(a[2].strip())), id=(int(a[1].strip()))) if a[-1] == "Savings Account" else
            StudentsAccount(owner=(a[0].strip()), amount=(float(a[2].strip())), id=(int(a[1].strip()))) if a[-1] == "Students Account" else
            CD(owner=(a[0].strip()), amount=(float(a[2].strip())), id=(int(a[1].strip()))) if a[-1] == "CD" else
            BankAccount(owner=(a[0].strip()), amount=(float(a[2].strip())), id=(int(a[1].strip())))
            )