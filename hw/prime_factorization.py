def die(error):
    raise Exception(error)


# Determine whether it is a prime number (easy version)
num = int(input("Please enter a number between 2~10000, this program will it's prime factorization :"))
if (num < 2) or (num > 10000):
    die("out of range")

# count = 0
i = 2
while i * i <= num:
    if num % i == 0:
        print(i)
        num /= i
    else:
        i += 1

print(int(num))
