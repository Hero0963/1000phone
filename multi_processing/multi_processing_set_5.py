# Python program to understand
# the concept of pool
import multiprocessing
import os


def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n * n)


def main():
    # input list
    mylist = [i for i in range(20)]

    # creating a pool object
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(square, mylist)

    print(result)


if __name__ == "__main__":
    main()
