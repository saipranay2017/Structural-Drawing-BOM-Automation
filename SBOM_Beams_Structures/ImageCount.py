try:
    class ImageCount:
        def __init__(self,count=0,dot_count=0):
            self.count = count
            self.dot_count = dot_count
        def set_count(self,count):
            self.count = count
        def get_count(self):
            return self.count
        def set_dot_count(self):
            self.dot_count = dot_count
        def get_dot_count(self):
            return dot_count
   
    imagecount = ImageCount()


except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
