def main_method():
    try:
        import traceback
        import cv2
        import easyocr
        from PIL import Image
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        import numpy as np
        import os
        from RecognizeCharacters import recognizecharacters
        from GetGreenBorderImage import get_image
        from GetTextFromImage import get_text_from_image
        import DataExtraction
        from extract_table_data import extract_drawing_details
        import InsertIntoExcel
        
        print("Generating Bill Of Materials")
        print()
        file=open("Filename.txt","r")
        file_name=file.readline()
        columns_image = file_name+".png"
        original_image = cv2.imread(columns_image)
        h,w,c = original_image.shape
        #print(h)
        #print(w)
        x = 1
        y = int(h/2)
        j = 2
        while x < w:
            pixel_color = original_image[y,x]
            if (pixel_color == [255,255,0]).all():
                #print(pixel_color)
                Right_Column_Image = original_image[:,x:]
                cv2.imwrite(f"{j}.png",Right_Column_Image)
                break
            x = x + 1
        count = 3
        Right_Column_Image = cv2.imread("2.png")
        # h,w,c = Right_Column_Image.shape
        # image = Right_Column_Image[int(h/2):,:]
        reader = easyocr.Reader(['en'])
        result = reader.readtext(Right_Column_Image)
        columndetails_objects = []
        columndetails_sections = []
        for j, detection in enumerate(result):
            flag = 0
            box = detection[0]
            x_min, y_min = int(box[0][0]), int(box[0][1])
            x_max, y_max = int(box[2][0]), int(box[2][1])
            if x_min < 0 or y_min < 0 or x_max > Right_Column_Image.shape[1] or y_max > Right_Column_Image.shape[0]:
                continue
            cropped_word = Right_Column_Image[y_min:y_max, x_min:x_max]
            if len(cropped_word) == 0:
                continue
            recognized_word = recognizecharacters.recognize_characters(cropped_word)
            if "CONN-" in recognized_word or "COLUMN" in recognized_word: #[y1:y2,x1:x2]
                #print(recognized_word)
                output = get_image(x_min,x_max,y_min,y_max,Right_Column_Image)
                if output == 1:
                    text = get_text_from_image()
                    columndetails_objects.extend(DataExtraction.data_formatting(text))
            if "PLATE" in recognized_word:
                output = get_image(x_min,x_max,y_min,y_max,Right_Column_Image)
                if output == 1:
                    text = get_text_from_image()
                    columndetails_objects.extend(DataExtraction.plate_data_formatting(text))
            elif "DRG" in recognized_word or "ORG" in recognized_word:
                #print(recognized_word)
                x_of  = x_min - 2
                x_min = x_min - 2
                y_min = y_min - 2
                y_of = y_min
            elif "SHEET" in recognized_word:
                x_min = x_min - 2
                y_min = y_min - 2
                simage = Right_Column_Image[y_min:y_max + 2,x_min: ]
                dimage = Right_Column_Image[y_of:y_min,x_of:]
                cv2.imwrite("LR/dnum.png",dimage)
                cv2.imwrite("LR/sheet.png",simage)
                os.system("python test.py")
                os.remove("LR/dnum.png")
                os.remove("LR/sheet.png")
            elif "REV" in recognized_word:
                rimage = Right_Column_Image[y_min-2:,x_min-2:]
                cv2.imwrite("LR/rev.png",rimage)
                os.system("python test.py")
                os.remove("LR/rev.png")
        for i in range(len(columndetails_objects)):
            columndetails_sections.append(columndetails_objects[i].get_section())
        columndetails_sections = list(set(columndetails_sections))
        #print(columndetails_sections)
        InsertIntoExcel.insert_pivot(columndetails_sections)
        Drawing_Details = extract_drawing_details()
        InsertIntoExcel.insert_drawing_details_into_excel(Drawing_Details[0],Drawing_Details[1],Drawing_Details[2])
        os.remove("cleat.png")
        os.remove("2.png")
        return 1
    except:
        traceback.print_exc()
        os.remove("cleat.png")
        os.remove("2.png")
        pdf_name = file_name + ".pdf"
        file.close()
        return pdf_name