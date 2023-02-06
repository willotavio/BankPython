from Log import *
from Bank import *
from Account import *
class Main:
    logger = Log()
    def __init__(self):
        nubank = Bank(1)
        while True:
            print("MENU"
                  "\nC.Create account"
                  "\nE.Exit")
            op = str(input().upper())
            if op == "C":
                accountName = str(input("Enter your account name: "))
                account = nubank.generateAccount(accountName)
                self.operateAccount(account)
            elif op == "E":
                break

    def operateAccount(self, account):
        print("Welcome " + account.accountName)
        while True:
            print("BANK"
                  "\n1.Deposit"
                  "\n2.Withdraw"
                  "\n3.View Balance"
                  "\n4.Break")
            choice = int(input())
            if choice == 1:
                print("DEPOSIT"
                      "\nEnter the value you want to deposit in your account:")
                account.deposit(float(input()))
            elif choice == 2:
                print("WITHDRAW"
                      "\nEnter the value you want to withdraw from your account:")
                if not account.withDraw(float(input())):
                    self.logger.out("Insufficient funds"
                               "\nCurrent balance: R$" + str(account.accountBalance))
                else:
                    self.logger.out("Withdraw successful"
                               "\nCurrent balance: R$" + str(account.accountBalance))

            elif choice == 3:
                account.getBalance()
            elif choice == 4:
                break

main = Main()