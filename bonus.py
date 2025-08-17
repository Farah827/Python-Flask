from Bank import BankAccount

class User:
    def __init__(self,name):
        self.name=name
        self.accounts={}


    def create_account(self,account_name,int_rate=0.01,balance=0):
        if account_name in self.accounts:
            raise ValueError(f"{account_name} account is already exists")
        else:
            self.accounts[account_name] = BankAccount(int_rate = int_rate , balance=balance)
        return self


    def make_deposit(self,amount,account_name):
        account= self.check_account(account_name)
        account.deposit(amount) 
        return self 


    def make_withdrawl(self,amount,account_name):
        account = self.check_account(account_name)
        account.withdraw(amount)
        return self


    def display_user_balance(self,account_name):
        account = self.check_account(account_name)
        print(f"name: {self.name} , {account_name} Balance: {account.balance}")   
        return self 
    

    def check_account(self,account_name):
        if account_name not in self.accounts:
            raise ValueError("account dosent exist")
        return self.accounts[account_name]


    

u1= User("farah")
u1.create_account("saveing",balance=1000)
u1.make_deposit(500,"saveing").make_withdrawl(100,"saveing").display_user_balance("saveing")    
            

