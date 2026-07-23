from csv import excel
from logging.config import valid_ident

balance = 1000

def deposit():
    global balance
    try:
        amt = float(input("enter amt to be deposited : "))
        balance += amt
        print(f"amount you deposited is {amt} and current balance is {balance}")
    except ValueError:
        print("give amount in float only or integers")
def send_money():
    global balance
    try:
        amt = float(input("enter amt to be send : "))
        balance -= amt
        print(f"amount you send is {amt} and current balance is {balance}")
    except ValueError:
        print("pls enter amy in float or integer only")
def check_balance():
    print(f"your current balance is : {balance}")

-----------------------------------------------------------------------------------------------------------------

import bank as b
from bank import deposit, send_money, check_balance


def user_bank():
    while(True):
        print("---------------welcome to bank--------------")
        print("chose your options\n","1.deposit money\n","2.send money\n","3.check balance\n","4.exit")
        c = int(input("enter your options here : "))
        match c:
            case 1 :
                deposit()
            case 2:
                send_money()
            case 3:
                check_balance()
            case 4:
                print("your are exiting application thank you")
                break
            case _:
                print("please enter correct input from given menu")


user_bank()


#To create user exception we have create a exception class first  and we have to raise manually.
#1.create exception class
#2. 