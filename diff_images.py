from PIL import Image
import math
import operator
from functools import reduce

def compare_images(path1, path2):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    diff = math.sqrt(reduce(operator.add, list(map(lambda a,b:(a-b)**2, histogram1, histogram2)))/len(histogram1))
    return diff

if __name__ == "__main__":
    image1 = r'I:\py\mywork\venv\image\imagedata\role4.png'
    image2 = r'I:\py\mywork\venv\image\imagedata\role9.png'
    a = compare_images(image1, image2)
    print(a)