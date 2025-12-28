try:
    import cv2
    import os
    import test
    from RecognizeCharacters import recognizecharacters
    class GetTextFromImage:
        def __init__(self,text='',flag=0,x_img_min=0):
            self.text = text
            self.flag = flag
            self.x_img_min = x_img_min
        def set_text(self,text):
            self.text = text
        def get_text(self,text):
            return self.text
        def set_flag(self,flag):
            self.flag = flag
        def get_flag(self):
            return self.flag
        def set_x_img_min(self,x_img_min):
            self.x_img_min = x_img_min
        def get_x_img_min(self):
            return self.x_img_min
   
    gettext = GetTextFromImage()
   
    def get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word):
        if end_word not in recognized_word and gettext.get_flag()==0:
            gettext.set_flag(1)
            gettext.set_x_img_min(x_min)
            return
        elif end_word in recognized_word:
            y_max = y_max + (y_max - y_min) + 4
            if gettext.get_flag()==1:
                bap_img = original_image[y_min:y_max,gettext.get_x_img_min():x_max]
            elif gettext.get_flag()==0:
                bap_img = original_image[y_min:y_max,x_min:x_max]
            cv2.imwrite(f'LR/bap.png',bap_img)
            os.system("python test.py")
            bap_img = cv2.imread(f'results/bap_rlt.png')
            bap_text = recognizecharacters.recognize_characters(bap_img)
            bap_text = bap_text.replace(' ','')
            bap_text = bap_text.replace('O','0')
            bap_text = bap_text.replace('o','0')
            os.remove(f'LR/bap.png')
            os.remove(f'results/bap_rlt.png')
            gettext.set_flag(0)
            gettext.set_x_img_min(0)
            return bap_text


except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
