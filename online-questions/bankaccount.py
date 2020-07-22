class BankAccount:
    def __init__(self,name):
        self.balance = 0
        self.name = name
        print("Hello! Welcome to this bank.")
    def deposit(self,amt):
        self.balance += amt
    def withdrawal(self,amt):
        if(amt<= self.balance):
            self.balance -= amt
            return ;
        print("Withdrawal unsuccessful.")
    def display(self):
        return self.balance
    def transfer(self,second,amt):
        if(self.balance >= amt):
            self.withdrawal(amt)
            second.deposit(amt)
        else:
            print("Transfer is not possible. ")
class fixedDeposit:
    def __init__(self,name1):
        self.amt = 0 
        self.name1 = name1 
    def deposit(self,amount):
        self.amt += amount
        print("Thank you for depositing your amount. ")
    def withdrawal(self):
        while(1 ):
           choice = input("Are you sure you want to break this Fixed deposit.Enter y or n?")
           if(choice.lower() == 'y' or choice.lower() == 'n'): break
        if(choice.lower() == 'y'):
            BankAccount.balance = self.amt
            return 1 ;
        print("Your amount is safe in fixed deposit. ")
    def balance(self):
        return self.amt 
name = input("Enter your name to create a bank account.")
bank1 = BankAccount(name)
bank1.deposit(100)
name1 = input("Enter your name to create fixed deposit. ")
bank2 = fixedDeposit(name1)
bank2.deposit(200)
if(bank2.withdrawal()):
    x = bank2.balance()
    bank2 = BankAccount(name1)
    bank2.deposit(x)
    if(name == name1):
        bank2.transfer(bank1,x)
print(bank1.display())
        
