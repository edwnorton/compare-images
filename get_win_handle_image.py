# -*- coding:utf-8 -*-
import ctypes
from PIL import ImageGrab
import win32gui

class WindowMgr():
    def __init__(self):
        '''Constructor'''
        self._handle = None

    def find_window(self, window_name, class_name=None):
        '''find a window by its window_name'''
        self._handle = win32gui.FindWindow(class_name, window_name)
        return self._handle

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]

    def __str__(self):
        return str((self.left, self.top, self.right, self.bottom))

w = WindowMgr()
HWND = w.find_window("夜神模拟器1")
if HWND == 0:
    print("找不到窗口")
    quit()
rect = RECT()
ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))
rangle = (rect.left, rect.top, rect.right, rect.bottom)
print(rangle)
a = r"I:\py\mywork\venv\image\t.png"
im = ImageGrab.grab(rangle)
im.save(a)
