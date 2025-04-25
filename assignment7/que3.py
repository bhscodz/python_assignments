import random
import csv

class Bank:
    @classmethod
    def load_accounts(cls):
        with open("acc_details.csv","r+") as f:
            data=csv.reader(f)
            data=list(data)
            data=data[1:]
            for i in data:
                cls.__init__(data[0],data[1])
    def __init__(self, acc, bal):
        self.acc=acc
        self.bal=bal
    def withdraw(self, amt):
        if amt>self.bal:
            print("oh! poor man you dont have that much money!!")
            print(f"current balance {self.bal}")
            return ''
        self.bal-=amt
        return f"Remaining Balance: {self.bal}"
    def deposit(self, amt):
        self.bal+=amt
        return f"Total Balance: {self.bal}"
    def display(self):
        print(f"Acc. Number: {self.acc}")
        print(f"Balance: {self.bal}")
def create_user():
    b=Bank(int(''.join([str(random.choice(range(10))) for i in range(6)])),200)
    user_acc[input("enter name of user")]=b
    print("user created successfuly")

b1=Bank(123456, 500)
b2=Bank(123210, 1000)
b3=Bank(987654, 300)
user_acc={"Dev":b1, "Mark":b2, "Andrew":b3}
name=input("Enter account name to proceed: ")
user=False
if name not in user_acc:
    print("user dosent exist")
    print("do you want to create user[y/n]")
    if input()=='y':
        create_user()
        user=True
    else:
        pass
    
else:
    user=True
while user:
   
    op=int(input('''Enter:
1.Withdraw
2.Deposit
3.Display
4.to quit\n'''))
    
    match op:
        case 1:
            amt = int(input("Enter amount: "))
            print(user_acc[name].withdraw(amt))
        case 2:
            amt = int(input("Enter amount: "))
            print(user_acc[name].deposit(amt))
        case 3:
            user_acc[name].display()
        case 4:
            print("quiting..")
            user=False
   