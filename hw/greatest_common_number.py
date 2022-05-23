print("Please enter two positive integers, a and b, the program will give their greatest common number:")
a = int(input("Please enter a:"))
b = int(input("Please enter b:"))

while b != 0:
    t = a % b
    a = b
    b = t

print("their gcd is %d." % a)
