import pyautogui as pg
import time


def write(s):
    pg.click(807, 979)
    pg.typewrite(s)
    pg.typewrite(["enter"])
    time.sleep(3)
    pg.click(1621, 896)
    pg.click(1621, 896)

    # time.sleep(1)
    pg.click(1693, 859)

    # time.sleep(1)
    pg.click(1014, 669)

    # time.sleep(1)
    pg.click(1111, 605)


print("please open a new txt file for full-screen in 10 seconds.")
time.sleep(10)

count = 2
while count >= 0:
    write("hello")

    if count == 0:
        write("finished")

    count -= 1

# ref= https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/
