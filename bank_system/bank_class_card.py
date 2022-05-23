class Card(object):
    def __init__(self, cardId, cardPasswd, cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMoney = cardMoney
        self.cardLock = False

    def LockCard(self):
        self.ccardLock = True

    def UnLockCard(self):
        self.ccardLock = False

    def isLocked(self):
        return self.cardLock

    def getCardMoney(self):
        return self.cardMoney

    def getMoney(self, money):
        if money <= 0:
            print("money <= 0 ")
            return False
        elif self.cardMoney < money:
            print("cardMoney < money ")
            return False
        else:
            self.cardMoney -= money
            return True

    def saveMoney(self, money):
        if money <= 0:
            print("money <= 0 ")
            return False
        elif money + self.cardMoney < self.cardMoney:
            print("card money will overflow ")
            return False
        else:
            self.cardMoney += money
            return True

    def changePasswd(self, newPasswd):
        self.cardPasswd = newPasswd
        return True
