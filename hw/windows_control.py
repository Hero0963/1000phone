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

while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(txtWindows, win32con.HWND_TOPMOST, x, y, 300, 300, win32con.SWP_SHOWWINDOW)
