import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

def get_image(x_min,x_max,y_min,y_max,img):
    ##print("Getting the Image")
    h,w,c = img.shape
    x_min = int((x_min+x_max)/2)
    x_max = int((x_min+x_max)/2)
    y_min = int((y_min+y_max)/2)
    y_max = int((y_min+y_max)/2)
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    x = x_max
    while x < w:
        pixel_color = img[y_min,x]
        if (pixel_color == [0,255,0]).all():
            # ##print(pixel_color)
            x2 = x
            break
        # else:
        #     x2 = w - 1
        x = x + 1
    x = x_min
    while x > 1:
        pixel_color = img[y_min , x]
        if (pixel_color == [0,255,0]).all():
            # #print(pixel_color)
            x1 = x
            break
        # else:
        #     x1 = 0
        x = x - 1
    y = y_min
    while y > 1:
        pixel_color = img[y ,x_min]
        if (pixel_color == [0,255,0]).all():
            # #print(pixel_color)
            y1 = y
            break
        # else:
        #     y1 = 0
        y = y - 1
    y = y_max
    while y < h:
        pixel_color = img[y ,x_min]
        if (pixel_color == [0,255,0]).all():
            # #print(pixel_color)
            y2 = y
            break
        # else:
        #     y2 = h - 1
        y = y + 1
    # #print("y1 y2 x1 x2")
    # #print(y1,y2,x1,x2)
    if x1>0 and x2>0 and y1>0 and y2>0:
        img1 = img[y1:y2,x1:x2]
        cv2.imwrite(f'cleat.png',img1)
        return 1
    else:
        return 0