class BankAccount:
    def __init__(self):
        self.balance = 0
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
    def __init__(self):
        self.amt = 0
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
bank1 = BankAccount()
bank1.deposit(100)
bank2 = BankAccount()
bank2.deposit(200)
bank2.transfer(bank1,bank2.display())
print(bank1.display())