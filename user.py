from Bank import BankAccount
class User:
    def __init__(self,name ,int_rate=0.01 , balance =0):
        self.name=name
        self.bankAccount = BankAccount(int_rate= int_rate , balance = balance)

    def make_withdrawal(self,amount):
        self.bankAccount.withdraw(amount)
        return self

    def make_deposit(self ,amount):
        self.bankAccount.deposit(amount)
        return self

    def display_user_balance(self):
        print(f"User:{self.name}")
        self.bankAccount.display_account_info()
        return self

    def transfer_money(self,user,amount):
        self.bankAccount.withdraw(amount)
        user.bankAccount.deposit(amount)
        print(f"{amount}$ trnsfered from {self.name} to {user.name}")
        return self                     
    
    
    
u1 = User("farah")
u1.make_deposit(1000).make_withdrawal(200).display_user_balance()