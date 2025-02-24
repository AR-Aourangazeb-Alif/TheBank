from random import randint


class customError(Exception):
    pass




class BankAccount:
    all = []
    account_count = 0

    def __init__(self, owner:str, amount:float, id=0):
        self.owner = owner
        self.balance = amount
        self.account_type = (
            "Checking Account" if self.__class__.__name__ == "CheckingAccount" else 
            "Savings Account" if self.__class__.__name__ == "SavingsAccount" else 
            "Students Account" if self.__class__.__name__ == "StudentsAccount" else
            "CD" if self.__class__.__name__ == "CD" else "Bank Account"
        )

        
        if id==0:
            while True:
                id = randint(115000000000000,115999999999999)
                id_doesn_exist = True
                for i in BankAccount.all:
                    if i.id == id:
                        id_doesn_exist = False
                        break
                if id_doesn_exist:
                    self.id = id
                    with open("accounts.csv", "a") as f:
                        f.write(f"{self.owner},{self.id},{self.balance},{self.account_type}\n")
                    break
        else:
            self.id = id


        BankAccount.all.append(self)
        BankAccount.account_count += 1

    
        
    

    ## validate transaction
    @staticmethod
    def validateTransaction(obj, amount):
        if amount <= obj.balance:
            return
        else:
            raise customError(f"Sorry, account '{obj.id}' only has a balance of ${obj.balance}")
        

    
    

    ## GEtting the account instance via the id
    @classmethod
    def getAccount(cls, id):
        for i in cls.all:
            if id == i.id:
                return i
        raise customError(f"No account with the ID: {id}")
    



    ## List accounts
    @classmethod
    def listAccounts(cls):
        print("   Owner             ID              Balance              Account Type\n")
        for i in cls.all:
            print(f"   {i.owner}       {i.id}       {i.balance}       {i.account_type}\n")      





    ## Getting balance
    @classmethod
    def getBalance(cls,id):
        try:
            a = cls.getAccount(id)
            return f"Account: {a.id}\nBalance: ${a.balance}"
        except customError as e:
            return f"Couldn't get data: {e}"
        




    ## Witdraw
    @classmethod
    def witdraw(cls, id, amount):
        try:
            account = cls.getAccount(id)

            cls.validateTransaction(obj=id, amount=amount)

            account -= amount

            a = "owner,id,balance,account_type\n"
            for i in cls.all:
                a += f"{i.owner},{i.id},{i.balance},{i.account_type}\n"
            with open("accounts.csv", "w") as f:
                f.write(a)

            return "Witdrawal complete"
        
        except customError as e:
            return f"Witdrawal failed: {e}"





    ## Transfer
    @classmethod
    def transfer(cls, frm_id, to_id, amount):
        try:
            frm = cls.getAccount(frm_id)
            to = cls.getAccount(to_id)

            cls.validateTransaction(obj=frm,amount=amount)

            frm.balance -= amount
            to.balance += amount

            a = "owner,id,balance,account_type\n"
            for i in cls.all:
                a += f"{i.owner},{i.id},{i.balance},{i.account_type}\n"
            with open("accounts.csv", "w") as f:
                f.write(a)

            return "Transfer complete"
        except customError as e:
            return f"Transaction interrupted: {e}"





    ## Deposite
    @classmethod
    def deposite(cls, id, amount):
        try:
            account = cls.getAccount(id)
            account.balance += amount
            a = "owner,id,balance,account_type\n"
            for i in cls.all:
                a += f"{i.owner},{i.id},{i.balance},{i.account_type}\n"
            with open("accounts.csv", "w") as f:
                f.write(a)

            return f"Deposite to complete"
        except customError as e:
            return f"Deposite interrupted: {e}"




        
    def __repr__(self):
        return f"{self.__class__.__name__}(Owner:'{self.owner}', Balance:{self.balance}, ID:{self.id})"
