# -*- coding:utf-8 -*-
import ctypes
import win32gui
import os
import math
import operator
from functools import reduce
from PIL import Image, ImageGrab, ImageEnhance


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


class Image_handle(object):
    def __init__(self):
        self.imdirpath = r"I:\py\mywork\venv\image\imagedata"

    def generateRoleImages(self, rolelist):
        for i in range(1, 12):
            image_name = "role" + str(i)
            image_path = os.path.join(self.imdirpath, image_name + ".png")
            im = ImageGrab.grab(rolelist[i-1])
            im = ImageEnhance.Brightness(im).enhance(1.5)
            im.save(image_path)

    def diff_images(self, image1_path, image2_path):
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        diff = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        return diff


def calculate(image1, image2):
    g = image1.histogram()
    s = image2.histogram()
    assert len(g) == len(s), "error"
    data = []
    for index in range(0, len(g)):
        if g[index] != s[index]:
            data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
        else:
            data.append(1)
    return sum(data) / len(g)


def split_imgae(image, part_size):
    pw, ph = part_size
    w, h = image.size
    sub_image_list = []
    assert w % pw == h % ph == 0, "error"
    for i in range(0, w, pw):
        for j in range(0, h, ph):
            sub_image = image.crop((i, j, i + pw, j + ph)).copy()
            sub_image_list.append(sub_image)
    return sub_image_list


def classfiy_histogram_with_split(image1, image2, size=(256, 256), part_size=(128, 128)):
    """ 'image1' and 'image2' is a Image Object.
    You can build it by 'Image.open(path)'.
    'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.
    'part_size' is size of piece what the image will be divided.It's 64*64 when it default.
    This function return the similarity rate betweene 'image1' and 'image2'
    """
    image1 = image1.resize(size).convert("RGB")
    sub_image1 = split_imgae(image1, part_size)
    image2 = image2.resize(size).convert("RGB")
    sub_image2 = split_imgae(image2, part_size)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    x = size[0] / part_size[0]
    y = size[1] / part_size[1]
    pre = round((sub_data / (x * y)), 3)
    return pre


w = WindowMgr()
HWND = w.find_window("夜神模拟器1")
if HWND == 0:
    print("找不到窗口")
    quit()
rect = RECT()
ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))
rangle = (rect.left, rect.top, rect.right, rect.bottom)
a = r"I:\py\mywork\venv\image\test.png"
role1 = (rect.left+55, rect.top+575, rect.left+55+64, rect.top+575+64)
role2 = (rect.left+55+64+64, rect.top+575, rect.left+55+64+64+64, rect.top+575+64)
role3 = (rect.left+55+128+128, rect.top+575, rect.left+55+128+128+64, rect.top+575+64)
role4 = (rect.left+55+192+192, rect.top+575, rect.left+55+192+192+64, rect.top+575+64)
role5 = (rect.left+118, rect.top+702, rect.left+118+64, rect.top+702+64)
role6 = (rect.left+118+64+64, rect.top+702, rect.left+118+64+64+64, rect.top+702+64)
role7 = (rect.left+118+128+128, rect.top+702, rect.left+118+128+128+64, rect.top+702+64)
role8 = (rect.left+55, rect.top+822, rect.left+55+64, rect.top+822+64)
role9 = (rect.left+55+64+64, rect.top+822, rect.left+55+64+64+64, rect.top+822+64)
role10 = (rect.left+55+128+128, rect.top+822, rect.left+55+128+128+64, rect.top+822+64)
role11 = (rect.left+55+192+192, rect.top+822, rect.left+55+192+192+64, rect.top+822+64)
rolelist = [eval("role" + str(i)) for i in range(1, 12)]


if __name__ == "__main__":
    n = 0
    res = 0
    while n < 20:
        n += 1
        Im = Image_handle()
        Im.generateRoleImages(rolelist)
        image_dict = {}
        Mypath = r"I:\py\mywork\venv\image\imagedata"

        for i in range(1, 12):
            name = "role" + str(i)
            image_path = os.path.join(Mypath, name + ".png")
            image_dict[i] = image_path
        for ind in range(1, 12):
            j = ind + 1
            while j < 12:
                # d = Im.diff_images(image_dict[ind], image_dict[j])
                im1 = Image.open(image_dict[ind])
                im2 = Image.open(image_dict[j])
                d = classfiy_histogram_with_split(im1, im2)
                print("{0} and {1} Similarity is {2}".format(ind, j, d))
                if d > 0.65:
                    res += 1
                    print("{0} and {1} is Same!".format(ind, j))
                    assert ind == 4 and j == 9, "The similar images are not 4 and 9"
                j += 1
    print("The num of similar images is {0}".format(res))
    assert res == 20, "some images wrong"
