year = int(input("Please enter a number(1582~3200), the system will"
                 " determine whether it is a leap year: "))

if (year < 1582) or (year > 3200):
    print("the number is out of range.")


if (year % 4) == 0 and (year % 100) != 0:
    print("This is a leap year.")
elif (year % 400) == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")