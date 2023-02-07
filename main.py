from Log import *
from Bank import *
from Account import *
class Main:
    logger = Log()
    def __init__(self):
        nubank = Bank(1)
        while True:
            print("MENU"
                  "\nL.List Accounts"
                  "\nC.Create Account"
                  "\nA.Access Account"
                  "\nE.Exit")
            op = str(input().upper())
            if op == "L":
                if not nubank.getAccounts():
                    self.logger.out("There's no account")
                else:
                    self.logger.out(nubank.getAccounts())
            elif op == "C":
                accountName = str(input("Enter your account name: "))
                accountPassword = str(input("Enter your account password: "))
                account = nubank.generateAccount(accountName, accountPassword)
                self.operateAccount(account)
            elif op == "A":
                self.logger.out(nubank.getAccounts())
                selectedName = input("Enter your account name: ")
                selectedPassword = input("Enter your account password: ")
                cc = nubank.accessAccount(selectedName, selectedPassword)
                if not cc:
                    self.logger.out("There's no account with this name")
                else:
                    self.operateAccount(cc)
            elif op == "E":
                break
            else:
                self.logger.out("Invalid option!\n"
                                "Try again")

    def operateAccount(self, account):
        print("Welcome " + account.accountName)
        while True:
            print("BANK"
                  "\nD.Deposit"
                  "\nW.Withdraw"
                  "\nB.View Balance"
                  "\nE.Exit")
            choice = str(input().upper())
            if choice == "D":
                print("DEPOSIT"
                      "\nEnter the value you want to deposit in your account:")
                account.deposit(float(input()))
            elif choice == "W":
                print("WITHDRAW"
                      "\nEnter the value you want to withdraw from your account:")
                if not account.withDraw(float(input())):
                    self.logger.out("Insufficient funds"
                               "\nCurrent balance: R$" + str(account.accountBalance))
                else:
                    self.logger.out("Withdraw successful"
                               "\nCurrent balance: R$" + str(account.accountBalance))

            elif choice == "B":
                account.getBalance()
            elif choice == "E":
                break

main = Main()