from Log import *
from Account import *
class Bank:
    logger = Log()

    bankAgency = ""
    accounts = []
    lastAccount = 1
    def __init__(self, bankAgency):
        self.bankAgency = bankAgency

    def generateAccount(self, accountName, accountPassword):
        account = Account(str(self.bankAgency), str(self.lastAccount), accountName, accountPassword, 0)
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

    def accessAccount(self, selectedName, selectedPassword):
        try:
            for i in range(len(self.accounts)):
                if getattr(self.accounts[int(i)], "accountName") == selectedName and getattr(self.accounts[int(i)], "accountPassword") == selectedPassword :
                    cc = self.accounts[int(i)]
                    return cc
        except:
            self.logger.out("ERROR")
