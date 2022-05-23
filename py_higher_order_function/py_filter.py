def is_odd(n):
    return n % 2 == 1


my_list = [x for x in range(11)]

tmp_list = filter(is_odd, my_list)
new_list = list(tmp_list)
print(new_list)
