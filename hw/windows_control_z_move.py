import datetime
import time
import win32con
import win32gui

txtWindows = win32gui.FindWindow("Notepad", "test001.txt - 記事本")

# parameter
x_0 = 400
y_0 = 200
x_1 = 800
y_1 = 500

t_1 = 5
t_2 = 5
t_3 = 5
time_gap = 0.5

time_start = time.time()
sum_t = 0

count = 0

while sum_t < t_1:
    x = x_0 + abs(x_1 - x_0) * (sum_t / t_1)
    y = y_0
    win32gui.SetWindowPos(txtWindows, win32con.HWND_TOPMOST, int(x), int(y), 300, 300, win32con.SWP_SHOWWINDOW)
    time.sleep(time_gap)
    time_Now = time.time()
    sum_t = (time_Now - time_start)
    count += 1
    # print(time_start, time_Now, sum_t, x, y, count)

time_start = time.time()
sum_t = 0
while sum_t < t_2:
    x = x_1 - abs(x_1 - x_0) * (sum_t / t_2)
    y = y_0 + abs(y_1 - y_0) * (sum_t / t_2)
    # print(time_start, time_Now, sum_t, x, y)
    win32gui.SetWindowPos(txtWindows, win32con.HWND_TOPMOST, int(x), int(y), 300, 300, win32con.SWP_SHOWWINDOW)
    time.sleep(time_gap)
    time_Now = time.time()
    sum_t = (time_Now - time_start)

time_start = time.time()
sum_t = 0
while sum_t < t_3:
    x = x_0 + abs(x_1 - x_0) * (sum_t / t_3)
    y = y_1
    # print(time_start, time_Now, sum_t, x, y)
    win32gui.SetWindowPos(txtWindows, win32con.HWND_TOPMOST, int(x), int(y), 300, 300, win32con.SWP_SHOWWINDOW)
    time.sleep(time_gap)
    time_Now = time.time()
    sum_t = (time_Now - time_start)
