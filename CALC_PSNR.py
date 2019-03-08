import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
#import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2
from tkinter import *
from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import ttk
import os
from PIL import Image
import subprocess
import cv2
import os
from PIL import Image
import subprocess
import shutil
import re
import math


def Compare(lis):                          # Mean Square Error.

    ans1 = 0.0
    ans2 = 0.0
    ans3 = 0.0

    psppp = int(1)

    for i in lis:
        print(psppp)
        psppp= psppp+1
        #print(i)
        p1 = Image.open(str("VSJH_IMAGES") + "\\" + str(i) + ".png")
        p2 = Image.open(str("VSJH_ORI") + "\\" + str(i) + ".png")
        width, height = p1.size
        for j in range(0,width):
            for k in range(0,height):
                r1,g1,b1 = p1.getpixel((j, k))
                r2, g2, b2 = p2.getpixel((j, k))

                x = abs(r1-r2)
                y = abs(g1-g2)
                z = abs(b1-b2)
                val1 = x*x
                val2 = y*y
                val3 = z*z
                ans1 += val1
                ans2 += val2
                ans3 += val3
    print(ans1,ans2,ans3)
    return ans1,ans2,ans3

# Driver Code
if __name__ == '__main__':


    # lis = [240,1427,3419,3929,2115,2586,1641,3321,2940,2136,824,1034,1425,2601,2249,3630,2121,944,2145,1365,1911,2841,3134,1982,3839,2669,270,3032,14,1172,2706,857, 2886, 3900, 2220, 3332, 3464, 1199, 809, 1082, 1439, 2160, 3105, 227, 1544, 2610, 212, 3359, 2700, 3467, 3932, 2414, 2624, 630, 3396, 1815, 525, 992, 171, 2490, 3726, 29]
    #
    # w = 1280		# Put WIDTH HERE
    #
    # h = 720         # Put HEIGHT HERE
    #
    # ansr,ansg, ansb = Compare(lis)
    #
    # l = int(len(lis))
	

    # a = ansr/(w*l*h)
    # b = ansg/(w*l*h)
    # c = ansb/(w*l*h)

    a =
    b =
    c =
	
    print("MSE for R,G,B")
    print(a,b,c)
	
	
    print("PSNR Valus for R,G,B")
    print(10 * math.log(((255*255) / (a)), 10))
    print(10 * math.log(((255*255) / (b)), 10))
    print(10 * math.log(((255*255) / (c)), 10))

