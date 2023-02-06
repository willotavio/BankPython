from Log import *
from Account import *
class Bank:
    logger = Log()

    bankAgency = ""
    accounts = []
    lastAccount = 1
    def __init__(self, bankAgency):
        self.bankAgency = bankAgency

    def generateAccount(self, accountName):
        print(self.lastAccount)
        account = Account(str(self.bankAgency), str(self.lastAccount), accountName, 0)
        self.lastAccount = self.lastAccount + 1
        return account

    def insertAccount(self, account):
        print(account)
        self.accounts.append(account)

    def getAccounts(self):
        return self.accounts

    def viewAccounts(self):
        for cc in self.accounts:
            print(cc)
