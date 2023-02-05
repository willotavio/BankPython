from Log import *
class Account:

    logger = Log()

    MAX_LENGHT = 12
    accountAgency = ""
    accountId = 0
    accountName = ""
    accountBalance = 0

    def __init__(self, accountAgency, accountId, accountName, accountBalance):
        self.accountAgency = accountAgency
        self.accountId = accountId
        self.setName(accountName)
        self.accountBalance = accountBalance

        self.logger.out("Account created!"
              "\nAgency: " + str(accountAgency) +
              "\nID: " + str(accountId) +
              "\nName: " + self.accountName +
              "\nBalance: " + str(accountBalance))

    def setName(self, accountName):
        if len(accountName) > self.MAX_LENGHT:
            self.accountName = accountName[0:self.MAX_LENGHT]
        else:
            self.accountName = accountName
        self.logger.out(self.accountName)

    def deposit(self, value):
        self.accountBalance = self.accountBalance + value
        self.logger.out("DEPOSIT - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))

    def withDraw(self, value):
        if(value > self.accountBalance):
            self.logger.out("WITHDRAW - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))
            accepted = False
            return accepted
        else:
            self.accountBalance = self.accountBalance - value
            self.logger.out("WITHDRAW - R$" + str(value) + " Current balance: R$" + str(self.accountBalance))
            accepted = True
            return accepted

    def getBalance(self):
        self.logger.out("BALANCE R$" + str(self.accountBalance))


