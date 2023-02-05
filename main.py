from Account import *
class Main:
    account = Account("01", 1, str(input("Enter your account name: ")), 0)
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
                  "\nEnter the value you want to withdraw from yout account:")
            account.withDraw(float(input()))
        elif choice == 3:
            account.getBalance()
        elif choice == 4:
            break
