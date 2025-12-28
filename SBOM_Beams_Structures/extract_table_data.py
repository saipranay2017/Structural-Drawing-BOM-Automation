def Extract_Table_Data():
    try:
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
        from InsertIntoExcel import insert_drawing_details
       
        reader = easyocr.Reader(['en'])
        count = 0
        # original_image = cv2.imread(f'results/dnum_rlt.png')
        # result = reader.readtext(f'results/dnum_rlt.png')
           
        text1 = ''
        word_image_path = f'results/dnum_rlt.png'
        recognized_word = recognizecharacters.recognize_characters(word_image_path)
        text1 = text1 + recognized_word
        drawingdetails.set_Drawing_Number('')
        drawingdetails.set_Sheet_Number('')
        drawingdetails.set_Revision_Number('')
        if "BEAM" in text1:    
            ind1 = text1.index("BEAM")
            drawingdetails.set_Drawing_Number(drawingdetails.get_Drawing_Number() + text1[ind1:ind1 + 4])
            ind1 = ind1 + 4
            drawingdetails.set_Drawing_Number(drawingdetails.get_Drawing_Number() + '/')
        elif "STRUCT" in text1:    
            ind1 = text1.index("STRUCT")
            drawingdetails.set_Drawing_Number(drawingdetails.get_Drawing_Number() + text1[ind1:ind1 + 6])
            ind1 = ind1 + 6
            drawingdetails.set_Drawing_Number(drawingdetails.get_Drawing_Number() + '/')
        while text1[ind1]!="P":
            ind1 = ind1 + 1
        for i in range(len(text1)-1,0,-1):
            if text1[i]=='.':
                s_index = i
                break
        s_index = s_index - 1
        temp = text1[s_index]
        text1 = text1.replace(temp,'S')
        drawingdetails.set_Drawing_Number(drawingdetails.get_Drawing_Number()+ text1[ind1:])
           
           
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
        drawingdetails.set_Sheet_Number(drawingdetails.get_Sheet_Number() + recognized_word[ind_sheet:])
           
           
        word_image_path = f'results/rev_rlt.png'
        recognized_word = recognizecharacters.recognize_characters(word_image_path)
        recognized_word = recognized_word.replace('O','0')
        recognized_word = recognized_word.replace('o','0')
        ind_rev1 = recognized_word.index("REV")
        ind_rev1 = ind_rev1 + 2
        recognized_word1 = recognized_word[ind_rev1:]
        ind_rev2 = recognized_word1.index('R')
        drawingdetails.set_Revision_Number(drawingdetails.get_Revision_Number() + recognized_word1[ind_rev2:])      
        insert_drawing_details(drawingdetails.get_Drawing_Number(),drawingdetails.get_Sheet_Number(),drawingdetails.get_Revision_Number())
    
    
    except Exception as e:
        print("ERROR OCCURED")
        print(e)
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()        
        os.remove(name+'.png')