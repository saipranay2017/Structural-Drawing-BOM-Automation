try:
    import easyocr
   
    reader = easyocr.Reader(['en'])
   
    class RecognizeCharacters:
        def recognize_characters(self,word_image):
            self.result = reader.readtext(word_image)
            self.recognized_text = ''
            for self.detection in self.result:
                self.box, self.text = self.detection[:2]
                self.recognized_text += self.text
            return self.recognized_text
   
    recognizecharacters = RecognizeCharacters()
except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
