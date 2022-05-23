import functools

mylist = [17, 22, 4, 6, 5]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, mylist))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, mylist))

# ref= https://www.geeksforgeeks.org/reduce-in-python/
