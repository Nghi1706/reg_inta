import os
import random
import re
import PIL
from PIL import Image

def avata():
    return r"E:\.Autoreg\Avata"+"\\"+str(random.choice(os.listdir(r'E:\.Autoreg\Avata')))

def status():
    return r"E:\.Autoreg\status"+"\\"+str(random.choice(os.listdir(r'E:\.Autoreg\status')))


def main():
    for count, filename in enumerate(os.listdir(r'C:\Users\GiaThuyStore2\Desktop\cloe\pic')):
        dst = "Mystatuspic" + str(count) + ".jpg"
        src = r'C:\Users\GiaThuyStore2\Desktop\cloe\pic' + "\\" + filename
        dst = r'C:\Users\GiaThuyStore2\Desktop\cloe\pic' + "\\" + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
