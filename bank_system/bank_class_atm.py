import random

from bank_class_user import User
from bank_class_card import Card


class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers

    def createUser(self):
        # dict={ID-user}
        name = input("Please enter your name: ")
        idCard = input("Please enter your idCard: ")
        phone = input("Please enter your phone number: ")

        prestoreMoney = int(input("Please enter your prestoreMoney: "))
        if prestoreMoney < 0:
            print("wrong prestoreMoney, create account fail...")
            return False

        onePasswd = int(input("Please set your passwd: "))
        if not self.checkPasswd(onePasswd):
            print("wrong password, create account fail...")
            return False

        strCardId = self.randomCardId()

        card = Card(strCardId, onePasswd, prestoreMoney)
        user = User(name, idCard, phone, card)

        self.allUsers[strCardId] = user

        print("Create account success ! Your cardId is %s , please remember.  " % strCardId)

    def searchUserInfo(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        print("cardID: %s  cardMoney: %d" % (user.card.cardId, user.card.cardMoney))

    def getMoney(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        cardMoney = user.card.getCardMoney()
        money = int(input("Your cardMoney is %d , please enter the money you want to get: " % cardMoney))
        if user.card.getMoney(money):
            print("get money success ")

    def saveMoney(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        money = int(input("Please enter the money you want to save: "))
        if user.card.saveMoney(money):
            print("save money success ")

    def transferMoney(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        tCardId = input("Please enter the CardID you want to transfer: ")
        tUser = self.allUsers.get(tCardId)
        if not tUser:
            print("no data...")
            return False

        money = int(input("Please enter the money you want to transfer: "))
        if money <= 0:
            print("money <= 0")
            return False

        if user.card.getMoney(money) and tUser.card.saveMoney(money):
            print("transfer money success")
            return True

    def changePasswd(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        newPasswd = int(input("Please reset your passwd: "))
        if not self.checkPasswd(newPasswd):
            print("wrong password, change passwd fail...")
            return False

        user.card.changePasswd(newPasswd)
        print("reset passwd success")

    def lockUser(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        user.card.LockCard()
        print("Card lock success !")

    def unlockUser(self):
        cardNum = input("Please enter your CardId: ")

        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        user.card.UnLockCard()
        print("Card unlock success !")

    def newCard(self):
        cardNum = input("Please enter your CardId: ")
        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if user.card.isLocked():
            print("This card is locked, please unlock first ")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        strNewCardId = self.randomCardId()

        newCard = Card(strNewCardId, user.card.cardPasswd, user.card.cardMoney)
        newUser = User(user.name, user.idCard, user.phone, newCard)

        self.allUsers[strNewCardId] = newUser
        del self.allUsers[cardNum]
        print("new card success, the old card data is deleted")

    def killUser(self):
        cardNum = input("Please enter your CardId: ")

        user = self.allUsers.get(cardNum)
        if not user:
            print("no data...")
            return False

        if not self.checkPasswd(user.card.cardPasswd):
            print(" wrong password...")
            return False

        del self.allUsers[user]
        print("delete user success")

    def checkPasswd(self, realPasswd):
        for i in range(3):
            tmpPasswd = int(input("Please enter your passwd: "))
            if tmpPasswd == realPasswd:
                return True
        return False

    def randomCardId(self):
        strCardId = ""
        n = 12

        # to avoid all numbers are used
        while True:
            for i in range(n):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                strCardId += ch

            if not self.allUsers.get(strCardId):
                return strCardId
