# -*- coding:utf-8 -*-
import ctypes
from PIL import ImageGrab
import win32gui
import os


class WindowMgr(object):
    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, window_name, class_name=None):
        """find a window by its window_name"""
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
# print(rangle)
a = r"I:\py\mywork\venv\image\test.png"
role1 = (rect.left+32, rect.top+555, rect.left+32+108, rect.top+555+108)
role2 = (rect.left+32+108+20, rect.top+555, rect.left+32+108+20+108, rect.top+555+108)
role3 = (rect.left+32+216+40, rect.top+555, rect.left+32+216+40+108, rect.top+555+108)
role4 = (rect.left+32+324+60, rect.top+555, rect.left+32+324+60+108, rect.top+555+108)
role5 = (rect.left+99, rect.top+678, rect.left+99+108, rect.top+678+108)
role6 = (rect.left+99+108+19, rect.top+678, rect.left+99+108+19+108, rect.top+678+108)
role7 = (rect.left+99+216+38, rect.top+678, rect.left+99+216+38+108, rect.top+678+108)
role8 = (rect.left+32, rect.top+801, rect.left+32+108, rect.top+801+108)
role9 = (rect.left+32+108+20, rect.top+801, rect.left+32+108+20+108, rect.top+801+108)
role10 = (rect.left+32+216+40, rect.top+801, rect.left+32+216+40+108, rect.top+801+108)
role11 = (rect.left+32+324+60, rect.top+801, rect.left+32+324+60+108, rect.top+801+108)
rolelist = [eval("role" + str(i)) for i in range(1, 12)]
print(rolelist)

imdirpath = r"I:\py\mywork\venv\image\imagedata"

def generateRoleImages(rolelist):

    for i in range(1, 12):
        image_name = "role" + str(i)
        image_path = os.path.join(imdirpath, image_name + ".png")
        print(image_path)
        im = ImageGrab.grab(rolelist[i-1])
        im.save(image_path)
generateRoleImages(rolelist)

