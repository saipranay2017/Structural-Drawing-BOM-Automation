def Image_Division():
    try:
        import cv2
        import easyocr
        from PIL import Image
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        import numpy as np
        import os
        from RecognizeCharacters import recognizecharacters
       
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()
       
        img_name = name + '.png'
        # Create an OCR reader
        reader = easyocr.Reader(['en'])
        result = reader.readtext(img_name)
        count = 1
        original_image = cv2.imread(img_name)
        h,w,c = original_image.shape
        x_of = 0
       
        for j, detection in enumerate(result):
            flag = 0
            box = detection[0]
            x_min, y_min = int(box[0][0]), int(box[0][1])
            x_max, y_max = int(box[2][0]), int(box[2][1])
            if x_min < 0 or y_min < 0 or x_max > original_image.shape[1] or y_max > original_image.shape[0]:
                continue
            cropped_word = original_image[y_min:y_max, x_min:x_max]
            if len(cropped_word) == 0:
                continue
            recognized_word = recognizecharacters.recognize_characters(cropped_word)
            if "MKD" in recognized_word: #[y1:y2,x1:x2]
                x1 = 0
                x2 = 0
                y1 = 0
                y2 = 0
                x = x_max
                while x < w:
                    pixel_color = original_image[y_min,x]
                    if (pixel_color == [0,255,0]).all():
                        x2 = x
                        break
                    else:
                        x2 = w - 1
                    x = x + 1
                x = x_min
                while x > 1:
                    pixel_color = original_image[y_min , x]
                    if (pixel_color == [ 0,255,0]).all():
                        x1 = x
                        break
                    else:
                        x1 = 0
                    x = x - 1
                y = y_min
                while y > 1:
                    pixel_color = original_image[y ,x_min]
                    if (pixel_color == [0,255,0]).all():
                        y1 = y
                        break
                    else:
                        y1 = 0
                    y = y - 1
                y = y_max
                while y < h:
                    pixel_color = original_image[y ,x_min]
                    if (pixel_color == [0,255,0]).all():
                        y2 = y
                        break
                    else:
                        y2 = h - 1
                    y = y + 1
                image = original_image[y1:y2,x1:x2]
                cv2.imwrite(f'{count}.png',image)
                count = count + 1
            elif "DRG" in recognized_word or "ORG" in recognized_word:
                x_of  = x_min - 2
                x_min = x_min - 2
                y_min = y_min - 2
                y_of = y_min
            elif "SHEET" in recognized_word:
                x_min = x_min - 2
                y_min = y_min - 2
                simage = original_image[y_min:y_max + 2,x_min: ]
                dimage = original_image[y_of:y_min,x_of:]
                cv2.imwrite("LR/dnum.png",dimage)
                cv2.imwrite("LR/sheet.png",simage)
            elif "REV" in recognized_word:
                rimage = original_image[y_min-2:,x_min-2:]
                cv2.imwrite("LR/rev.png",rimage)
     
        os.system("python test.py")
        os.remove("LR/dnum.png")
        os.remove("LR/sheet.png")
        os.remove("LR/rev.png")
        return count
    
    
    except Exception as e:
        print("ERROR OCCURED")
        print(e)
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()        
        os.remove(name+'.png')
