# ref=https://www.geeksforgeeks.org/synchronization-pooling-processes-python/


# Python program to illustrate
# the concept of locks
# in multiprocessing
import multiprocessing


# function to withdraw from account
def withdraw(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value = balance.value - 1


# function to deposit to account
def deposit(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value = balance.value + 1


def perform_transactions():
    # initial balance (in shared memory)
    balance = multiprocessing.Value('i', 100)

    # creating a lock object
    lock = multiprocessing.Lock()

    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    # starting processes
    p1.start()
    p2.start()

    # wait until processes are finished
    p1.join()
    p2.join()

    # print final balance
    print("Final balance = {}".format(balance.value))


def main():
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()


if __name__ == "__main__":
    main()
