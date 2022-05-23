import os


def getAllDir(path, sp=""):
    fileList = os.listdir(path)
    sp += "   "
    for fileName in fileList:
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "catalog: ", fileName)
            getAllDir(fileAbsPath, sp)
        else:
            print(sp + "general file: ", fileName)


getAllDir(r"D:\PythonProject\first")
