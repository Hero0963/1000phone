import random

print("This program will generate a verification code with 6 chars:")

n = 6
idx = 0
strOutput = ""
r = 0
asciiCode = 0

while idx < n:
    r = random.choice(range(9 + 26 + 26))
    if 0 <= r <= 9:
        asciiCode = (r - 0) + ord("0")
    elif 10 <= r <= 35:
        asciiCode = (r - 10) + ord("A")
    else:
        asciiCode = (r - 36) + ord("a")

    print(asciiCode)
    strOutput += chr(asciiCode)
    idx += 1

print(strOutput)
