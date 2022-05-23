import math
import random
import time

import win32api
import win32con
import win32gui

# win32api.MessageBox(win32con.NULL, 'Hello Hello Hello Hello Hello！', 'Hello', win32con.MB_OK)


txtWindows = win32gui.FindWindow("Notepad", "test001.txt - 記事本")

# while True:
#     win32gui.ShowWindow(txtWindows, win32con.SW_HIDE)
#     time.sleep(2)
#     win32gui.ShowWindow(txtWindows, win32con.SW_SHOW)
#     time.sleep(2)

# parameter
x_0 = 500
y_0 = 300

r = 200
theta = 0
step = 12
time_gap = 0.25
time_end = 5

time_start = time.time()
sum_t = 0

while sum_t < time_end:
    theta = theta + (2 * math.pi) / step
    x = x_0 + r * math.cos(theta)
    y = y_0 + r * math.sin(theta)
    win32gui.SetWindowPos(txtWindows, win32con.HWND_TOPMOST, int(x), int(y), 300, 300, win32con.SWP_SHOWWINDOW)
    time.sleep(time_gap)
    time_Now = time.time()
    sum_t = (time_Now - time_start)
    # print(time_start, time_Now, sum_t)
