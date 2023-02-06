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
        self.insertAccount(account)
        return account

    def insertAccount(self, account):
        self.accounts.append(account)

    def getAccounts(self):
        if len(self.accounts) == 0:
            return False
        else:
            accountList = []
            for i in self.accounts:
                accountList.append(str(i.accountAgency) + "/" + str(i.accountId) + "/" + str(i.accountName) + "/" + str(i.accountBalance))
            return accountList

    def accessAccount(self, selectedId):
        try:
            cc = self.accounts[int(selectedId) - 1]
            return cc
        except:
            self.logger.out("ERROR")
