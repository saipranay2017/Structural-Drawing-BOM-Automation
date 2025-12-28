import cv2
import easyocr
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from RecognizeCharacters import recognizecharacters

def get_text_from_image():
    #print("Getting text from image")
    cleat = cv2.imread("cleat.png")
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cleat)
    text = ''
    for j, detection in enumerate(result):
        flag = 0
        box = detection[0]
        x_min, y_min = int(box[0][0]), int(box[0][1])
        x_max, y_max = int(box[2][0]), int(box[2][1])
        if x_min < 0 or y_min < 0 or x_max > cleat.shape[1] or y_max > cleat.shape[0]:
            continue
        cropped_word = cleat[y_min:y_max, x_min:x_max]
        if len(cropped_word) == 0:
            continue
        cv2.imwrite(f"LR/word_{j+1}.png",cropped_word)
        os.system("Python test.py")
        cleat1 = cv2.imread(f"results/word_{j+1}_rlt.png")
        recognized_word = recognizecharacters.recognize_characters(cleat1)
        #print("recognized_word:",recognized_word)
        text = text + recognized_word
        os.remove(f"LR/word_{j+1}.png")
        os.remove(f"results/word_{j+1}_rlt.png")
    return text

# get_text_from_image()