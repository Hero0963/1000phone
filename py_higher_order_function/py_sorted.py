my_list = [3, 25, -14, -11, 21, 13, 7.0]

print("Sorted List returned :"),
print(sorted(my_list))

print("\nReverse sort :"),
print(sorted(my_list, reverse=True))

print("\nOriginal list not modified :"),
print(my_list)

print("\nSorted by abs value :"),
print(sorted(my_list, key=lambda x: x * x))

# ref= https://www.geeksforgeeks.org/sorted-function-python/
