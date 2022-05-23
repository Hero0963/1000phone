import time


class Admin(object):
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("****************************************************")
        print("*                                                  *")
        print("*                                                  *")
        print("*                                                  *")
        print("*                                                  *")
        print("*   Welcome to HERO BANK                           *")
        print("*                                                  *")
        print("*                                                  *")
        print("*                                                  *")
        print("*                                                  *")
        print("****************************************************")

    def adminOption(self):
        inputAdmin = input("Please enter adminID: ")
        if self.admin != inputAdmin:
            print(" wrong adminID")
            return False

        inputPasswd = input("Please enter password: ")
        if self.passwd != inputPasswd:
            print(" wrong password")
            return False

        print("success, please wait...")
        time.sleep(2)
        return True

    def printSystemFunctionView(self):
        print("****************************************************")
        print("*                                                  *")
        print("*                 HERO  BANK                       *")
        print("*                                                  *")
        print("*    open(0)      search(1)      get(2)            *")
        print("*    save(3)      transfer(4)    changePWD(5)      *")
        print("*    lock(6)      unlock(7)      new(8)            *")
        print("*    delete(9)    quit(q)                          *")
        print("*                                                  *")
        print("*                                                  *")
        print("*                                                  *")
        print("****************************************************")








