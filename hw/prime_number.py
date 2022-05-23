def die(error):
    raise Exception(error)


# Determine whether it is a prime number (easy version)
num = int(input("Please enter a number between 2~10000, this program will show whether it is a prime number:"))
if (num < 2) or (num > 10000):
    die("out of range")

# count = 0
i = 2
flag = True
while i * i < num and (flag is True):
    if num % i == 0:
        print("%d is not a prime number, it can be divided by %d" % (num, i))
        flag = False
    i += 1
    # count += 1

# print(count)

if flag is True:
    print("%d is a prime number." % num)
