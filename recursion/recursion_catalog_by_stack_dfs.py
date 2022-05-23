import os.path


def getAllDirDeep(path):
    stack = []
    stack.append(path)

    while len(stack) != 0:
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)

        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("catalog: " + fileName)
                stack.append(fileAbsPath)
            else:
                print("general file: " + fileName)


getAllDirDeep(r"D:\PythonProject\first")
