# ref=https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:
        # message received from server
        data = c.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', str(data.decode()))

        message = input("You want to send: ")
        # message sent to server
        c.send(message.encode())

    # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 7414
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

    s.close()


if __name__ == '__main__':
    Main()
