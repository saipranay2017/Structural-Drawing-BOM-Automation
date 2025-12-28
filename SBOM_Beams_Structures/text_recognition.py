def Text_Recognition():
    try:
        import os
        import cv2
        import easyocr
        from PIL import Image
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        import numpy as np
        import BeamDetails
        import AngleCleatDetails
        import PlateDetails
        import MarkedNumbers
        from RecognizeCharacters import recognizecharacters
        import GetTextFromImage
        import InsertIntoExcel
        from image_division import Image_Division
        imagecount = Image_Division()
        from extract_table_data import Extract_Table_Data
        Extract_Table_Data()
        
        reader = easyocr.Reader(['en'])
        beams = []
        angle_cleats = []
        plates = []
        # mkd_flag = 0
        # mkd_list = []
        # to_flag = 0
        # to_starting_mkd = ''
        # for i in range(1,2):
        for i in range(1,imagecount):
            ism_flag = 0
            ism_list = []
            isa_flag = 0
            isa_list = []
            plt_flag = 0
            plt_list = []
            mkd_flag = 0
            mkd_list = []
            to_flag = 0
            to_starting_mkd = ''
            result = reader.readtext(str(i)+'.png')
            original_image = cv2.imread(str(i)+'.png')
            for j, detection in enumerate(result):
                box = detection[0]
                x_min, y_min = int(box[0][0]), int(box[0][1])
                x_max, y_max = int(box[2][0]), int(box[2][1])
                if x_min < 0 or y_min < 0 or x_max > original_image.shape[1] or y_max > original_image.shape[0]:
                    continue
                cropped_word = original_image[y_min:y_max, x_min:x_max]
                if len(cropped_word) == 0:
                    continue
                cv2.imwrite(f'LR/word_{j+1}.png', cropped_word)
                os.system("python test.py")
                os.remove(f'LR/word_{j+1}.png')
                word_image_path = f'results/word_{j+1}_rlt.png'
                word_image = cv2.imread(word_image_path)
                recognized_word = recognizecharacters.recognize_characters(word_image)
                os.remove(f'results/word_{j+1}_rlt.png')
                if "ISMB" in recognized_word or "ISMC" in recognized_word or ism_flag==1:
                    end_word = "Lg"
                    ism_flag = 1
                    if end_word not in recognized_word:
                        GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        continue    
                    else:
                        ism_text = GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        ism_list.append(BeamDetails.get_ism_details(ism_text))
                        for f in range(len(ism_list)):
                            beams.append(ism_list[f].get_beam_section())
                        ism_flag = 0
                if "ISA" in recognized_word or isa_flag==1:
                    end_word = "THK"
                    if end_word not in recognized_word:
                        isa_flag=1
                        GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        continue
                    else:
                        isa_text = GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        isa_flag=0
                    isa_list.append(AngleCleatDetails.get_angle_cleat_details(isa_text))
                    for f in range(len(isa_list)):
                        angle_cleats.append(isa_list[f].get_angle_cleat_section())
                if "PLT" in recognized_word or plt_flag==1:
                    end_word = "THK"
                    if end_word not in recognized_word:
                        GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        plt_flag = 1
                        continue
                    else:
                        plt_text = GetTextFromImage.get_text_from_image(original_image,x_min,x_max,y_min,y_max,recognized_word,end_word)
                        plt_flag = 0
                    plt_list.append(PlateDetails.get_plate_details(plt_text))
                    for f in plt_list:
                        plates.append(f.get_plate_thickness())
                if "MKD" in recognized_word or mkd_flag==1:
                    if recognized_word[-3:]=="MKD" or recognized_word[-4:-1]=="MKD":
                        mkd_flag = 1
                        continue
                    elif "," in recognized_word:
                        if mkd_flag == 0:
                            mkd_index = recognized_word.index("MKD")
                            mkd_index = mkd_index + 3
                            while recognized_word[mkd_index].isalnum()==False:
                                mkd_index = mkd_index + 1
                            mkd_list.extend(MarkedNumbers.get_mkd_comma_seperated(recognized_word[mkd_index:],mkd_flag))
                        elif mkd_flag == 1:
                            mkd_list.extend(MarkedNumbers.get_mkd_comma_seperated(recognized_word,mkd_flag))
                    elif "TO" in recognized_word or "T0" in recognized_word or to_flag==1:
                        mkd_list = []
                        recognized_word = recognized_word.replace(' ','')
                        getVals = list([val for val in recognized_word if val.isalpha()])
                        res = "".join(getVals)
                        if res == "TO" or res == "To" or res == "T0":
                            to_starting_mkd = to_starting_mkd + "TO"
                            to_flag = 1
                            continue
                        elif res[:2]=="TO" or res[:2]=="To" or res[:2]=="T0":
                            to_starting_mkd = to_starting_mkd + recognized_word
                            mkd_list.extend(MarkedNumbers.get_mkd_to_seperated(to_starting_mkd,mkd_flag))
                        elif res[-2:]=="TO" or res[-2:]=="To" or res[-2:]=="T0":
                            mkd_index = recognized_word.index("MKD")
                            mkd_index = mkd_index + 3
                            while recognized_word[mkd_index].isalnum()==False:
                                mkd_index = mkd_index + 1
                            to_starting_mkd = to_starting_mkd + recognized_word[mkd_index:]
                            to_flag = 1
                            mkd_flag = 1
                        elif mkd_flag == 1 and to_flag==0:
                            to_starting_mkd = to_starting_mkd + recognized_word
                            mkd_list.extend(MarkedNumbers.get_mkd_to_seperated(to_starting_mkd,mkd_flag))
                        elif mkd_flag==1 and to_flag==1:
                            to_starting_mkd = to_starting_mkd + recognized_word
                            mkd_list.extend(MarkedNumbers.get_mkd_to_seperated(to_starting_mkd,mkd_flag))
                            to_flag = 0
                        elif mkd_flag == 0 and to_flag==0:
                            mkd_index = recognized_word.index("MKD")
                            mkd_index = mkd_index + 3
                            while recognized_word[mkd_index].isalnum()==False:
                                mkd_index = mkd_index + 1
                            mkd_list.extend(MarkedNumbers.get_mkd_to_seperated(recognized_word[mkd_index:],mkd_flag))
                    else:
                        if mkd_flag == 0:
                            mkd_index = recognized_word.index("MKD")
                            mkd_index = mkd_index + 3
                            while recognized_word[mkd_index].isalnum()==False:
                                mkd_index = mkd_index + 1
                            mkd_list.extend(MarkedNumbers.get_mkd(recognized_word[mkd_index:],mkd_flag))
                        elif mkd_flag == 1:
                            mkd_list.extend(MarkedNumbers.get_mkd(recognized_word,mkd_flag))
                        to_starting_mkd = to_starting_mkd + mkd_list[-1]
                        mkd_flag = 1
            os.remove(str(i)+'.png')
            #print("MKD list: ",mkd_list)
            for mkd in mkd_list:
                for ism in ism_list:
                    InsertIntoExcel.insert_beam_into_excel(i,mkd,ism)
                for isa in isa_list:
                    InsertIntoExcel.insert_angle_cleat_into_excel(i,mkd,isa)
                for plt in plt_list:
                    InsertIntoExcel.insert_plate_into_excel(i,mkd,plt)
        beams = list(set(beams))
        angle_cleats = list(set(angle_cleats))
        plates = list(set(plates))
        # print("Unique beams:",beams)
        # print("Unique angle_cleats:",angle_cleats)
        # print("Unique plates:",plates)
        InsertIntoExcel.insert_pivot(beams)
        InsertIntoExcel.insert_pivot(angle_cleats)
        InsertIntoExcel.insert_pivot(plates)
        InsertIntoExcel.insert_pivot_total()
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()
        if os.path.isfile(name+'.png'):
            os.remove(name+'.png')        
        print()
        print("Bill Of Materails Generated Successfully for: ")
        static_index = name.index("static/")
        static_index = static_index + 7
        print("Drawing: "+name[static_index:]+".pdf")
        return 1
      
    except Exception as e:
        print(e)
        print("ERROR OCCURED in text_recogntion")
        with open("workbook.pkl", "rb") as file:
            workbook = pickle.load(file)
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()      
        os.remove(name+'.png')
        pdf_name = name + '.pdf'
        return pdf_name
