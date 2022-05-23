"""
Person
property: Name/Tel/Card/ID
behavior:

Card
property: ID/ pwd/ money


ATM
behavior: open/search/save/get/change pwd/......


Bank

Admin

"""
import os
import time
import pickle

from bank_class_admin import Admin
from bank_class_atm import ATM
from bank_class_const import Const


def main():
    admin = Admin()

    admin.printAdminView()

    if not admin.adminOption():
        return False

    filePath = os.path.join(os.getcwd(), "alluser.txt")
    f = open(filePath, "rb")
    allUsers = pickle.load(f)
    f.close()

    atm = ATM(allUsers)

    while True:
        admin.printSystemFunctionView()
        option = input("Please pick an option: ")

        if option == Const.StrOpen:
            print("open(0) ")
            atm.createUser()

        elif option == Const.StrSearch:
            print("search(1) ")
            atm.searchUserInfo()

        elif option == Const.StrGet:
            print("get(2) ")
            atm.getMoney()

        elif option == Const.StrSave:
            print("save(3) ")
            atm.saveMoney()

        elif option == Const.StrTransfer:
            print("transfer(4) ")
            atm.transferMoney()

        elif option == Const.StrChangePWD:
            print("changePWD(5) ")
            atm.changePasswd()

        elif option == Const.StrLock:
            print("lock(6) ")
            atm.lockUser()

        elif option == Const.StrUnlock:
            print("unlock(7) ")
            atm.unlockUser()

        elif option == Const.StrNew:
            print("new(8) ")
            atm.newCard()

        elif option == Const.StrDelete:
            print("delete(9) ")
            atm.killUser()

        elif option == Const.StrQuit:
            print("quit(q) ")
            if admin.adminOption():
                f = open(filePath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                break

        time.sleep(1.5)


if __name__ == '__main__':
    main()
