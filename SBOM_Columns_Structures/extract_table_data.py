import cv2
import easyocr
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import pickle
from DrawingDetails import drawingdetails
from RecognizeCharacters import recognizecharacters
# import InsertIntoExcel

def extract_drawing_details():
    reader = easyocr.Reader(['en'])
    count = 0 
    original_image = cv2.imread(f'results/dnum_rlt.png')
    result = reader.readtext(f'results/dnum_rlt.png')
    Drawing_Number = ''
    text1 = ''
    for j, detection in enumerate(result):
        box = detection[0]
        count = count + 1
        x_min, y_min = int(box[0][0]), int(box[0][1])
        x_max, y_max = int(box[2][0]), int(box[2][1])
        
        # Crop the word region from the original image
        cropped_word = original_image[y_min:y_max, x_min:x_max]
        
        # Save the cropped word as a separate image
        cv2.imwrite(f'LR/word_{j+1}.png', cropped_word)
        
    os.system("python test.py")
    
    for k in range(1,count + 1):  # Assuming num_word_images is the total number of word images
        word_image_path = f'results/word_{k}_rlt.png'
        word_image = cv2.imread(word_image_path)
        recognized_word = recognizecharacters.recognize_characters(word_image)
        os.remove(f'LR/word_{k}.png')
        os.remove(f'results/word_{k}_rlt.png')
        text1 = text1 + recognized_word
        #print(text1)
    if "BEAM" in text1:    
        ind1 = text1.index("BEAM")
        Drawing_Number = Drawing_Number + text1[ind1:ind1 + 4]
        ind1 = ind1 + 4
        Drawing_Number = Drawing_Number + '/'
    elif "STRUCT" in text1:    
        ind1 = text1.index("STRUCT")
        Drawing_Number = Drawing_Number + text1[ind1:ind1 + 6]
        ind1 = ind1 + 6
        Drawing_Number = Drawing_Number + '/'
    while text1[ind1]!="P":
        ind1 = ind1 + 1
    for i in range(len(text1)-1,0,-1):
        if text1[i]=='.':
            s_index = i
            break
    left_index = s_index - 1
    if text1[left_index] != "S":
        text1 = text1[:left_index] + "S" + text1[s_index:]
    right_index = s_index + 1
    if "S" in text1[right_index:]:
        temp = text1[right_index:]
        temp = temp.replace("S","5")
        text1 = text1[:s_index+1] + temp  
    Drawing_Number = Drawing_Number + text1[ind1:]
    
    
    word_image_path = f'results/sheet_rlt.png'
    recognized_word = recognizecharacters.recognize_characters(word_image_path)
    if "NO" in recognized_word: 
        ind_sheet = recognized_word.index("NO")
    elif "No" in recognized_word:
        ind_sheet = recognized_word.index("No")
    elif "N0" in recognized_word:
        ind_sheet = recognized_word.index("N0")
    ind_sheet = ind_sheet + 2
    if recognized_word[ind_sheet]==',' or recognized_word[ind_sheet]=='.':
        ind_sheet = ind_sheet + 1
    if 'I' in recognized_word:
        recognized_word = recognized_word.replace('I','')
    if 'l' in recognized_word:
        recognized_word = recognized_word.replace('l','')
    Sheet_Number = recognized_word[ind_sheet:]
    #print("Drawing_Number:",Drawing_Number)
    #print("Sheet_Number:",Sheet_Number)
    
    word_image_path = f'results/rev_rlt.png'
    recognized_word = recognizecharacters.recognize_characters(word_image_path)
    recognized_word = recognized_word.replace('O','0')
    recognized_word = recognized_word.replace('o','0')
    ind_rev1 = recognized_word.index("REV")
    ind_rev1 = ind_rev1 + 2
    recognized_word1 = recognized_word[ind_rev1:]
    ind_rev2 = recognized_word1.index('R')
    Revision_Number = recognized_word1[ind_rev2:]
    #print("Revision Number:",Revision_Number)       
    Drawing_Details = [Drawing_Number,Sheet_Number,Revision_Number] 
    return Drawing_Details

# extract_drawing_details()