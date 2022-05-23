# Print Narcissistic numbers between 100~999
print(r"this program will print all Narcissistic numbers between 100~999:")

n = 100
copyNum = 0
uDigit = 0
tDigit = 0
hDigit = 0
sumVal = 0
while n < 1000:
    copyNum = n

    uDigit = (copyNum % 10)

    copyNum //= 10
    tDigit = (copyNum % 10)

    copyNum //= 10
    hDigit = (copyNum % 10)

    sumVal = (hDigit ** 3) + (tDigit ** 3) + (uDigit ** 3)
    if sumVal == n:
        print(n)

    n += 1
