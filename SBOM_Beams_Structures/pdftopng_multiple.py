def pdf_to_png(pdf_file):
    try:
        from pdf2image import convert_from_path
        import os
        import glob
        import pickle
        from text_recognition import Text_Recognition
        pdf = "static/" + pdf_file
        ind = pdf.index('.pdf')
        file_name = pdf[:ind]
        img_name = file_name + '.png'
        file = open("FileName.txt","w")
        file.write(file_name)
        file.close()
        images = convert_from_path(pdf,poppler_path="C:/Program Files/poppler-24.02.0/Library/bin")
        for i in range(len(images)):
            images[i].save(img_name, 'PNG')
        returned = Text_Recognition()
        return returned
        #os.system("python text_recognition.py")


    except Exception as e:
        print("ERROR OCCURED")
        print(e)
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()
        if os.path.isfile(name+'.png'):
            os.remove(name+'.png')
        pdf_name = name + '.pdf'
        return pdf_name