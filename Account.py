from Log import *
class Account:

    logger = Log()

    MAX_LENGTH = 12
    MIN_LENGTH = 8

    def __init__(self, accountAgency, accountId, accountName, accountPassword, accountBalance):
        self.accountAgency = accountAgency
        self.accountId = accountId
        self.setName(accountName)
        self.setPassword(accountPassword)
        self.accountBalance = accountBalance
        self.logger.out("Account created!"
              "\nAgency: " + str(accountAgency) +
              "\nID: " + str(accountId) +
              "\nName: " + self.accountName +
              "\nBalance: " + str(accountBalance))

    def setName(self, accountName):
        if len(accountName) > self.MAX_LENGTH:
            self.accountName = accountName[0:self.MAX_LENGTH]
        else:
            self.accountName = accountName
        self.logger.out(self.accountName)

    def setPassword(self, accountPassword):
        self.accountPassword = accountPassword
    def deposit(self, value):
        self.accountBalance = self.accountBalance + value
        self.logger.out("DEPOSIT - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))

    def withDraw(self, value):
        if value > self.accountBalance:
            self.logger.out("WITHDRAW - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))
            return False
        else:
            self.accountBalance = self.accountBalance - value
            self.logger.out("WITHDRAW - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))
            return True

    def getBalance(self):
        self.logger.out("BALANCE R$" + str(self.accountBalance))
