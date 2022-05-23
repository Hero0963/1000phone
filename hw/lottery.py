import  random
num = int(input("Please enter a number( 1~100) :"))

r = random.choice(range(100)) + 1

if num == r:
    print("Congrats!")
else:
    print("You are not lucy, the lottery number is: ", r)