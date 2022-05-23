def sum1(n):
    s = 0
    for x in range(1, n + 1):
        s += x

    return s


def sum2(n):
    if n == 1:
        return 1
    else:
        return sum2(n - 1) + n


res1 = sum1(5)
print(res1)

res2 = sum2(5)
print(res2)

