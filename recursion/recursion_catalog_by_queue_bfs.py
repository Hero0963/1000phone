import os
import collections


def getAllDirQu(path):
    queue = collections.deque()

    queue.append(path)

    while len(queue) != 0:
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)

        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("catalog: " + fileName)
                queue.append(fileAbsPath)
            else:
                print("general file: " + fileName)


getAllDirQu(r"D:\PythonProject\first")
