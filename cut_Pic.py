from PIL import ImageGrab

def cut_Pic(box, outfile):
    im = ImageGrab.grab(box)
    im.save(outfile)
if __name__ == '__main__':
    bbox1 = (416,555,524,663)
    outfile = r'I:\py\mywork\venv\image\t.png'
    cut_Pic(bbox, outfile)