"""
ref=https://shengyu7697.github.io/python-read-text-file/
ref=https://shengyu7697.github.io/python-write-text-file/

goal: read hw20220103.txt, parse email and save as pemail20220103.txt

"""

path = "hw20220103.txt"
outputPath = "pemail20220103.txt"
of = open(outputPath, 'w')

with open(path) as f:
    for line in f.readlines():
        s = line.split(' ')
        for t in s:
            if "@" in t and ".com" in t:
                of.write(t)

of.close()
