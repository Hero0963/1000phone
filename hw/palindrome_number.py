# Print palindrome numbers between 10000~99999
print(r"This program will print all palindrome numbers between 10000 ~ 99999:")

count = 0
num = 10000
copyNum = 10000

v1 = v2 = v4 = v5 = 0

while num < 100000:
    copyNum = num

    v1 = copyNum % 10
    v5 = copyNum // 10000
    if v1 == v5:
        copyNum //= 10
        v2 = copyNum % 10
        v4 = copyNum // 1000
        if v2 == v4:
            print(num)
            count += 1

    num += 1

print("There are %d many palindrome numbers." % count)
