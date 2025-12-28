try:
    class PlateDetails:
        def __init__(self,Plate_Thickness='',Plate_Dimensions='',Plate_Quantity=0,Plate_Standard_Weight=7.85):
            self.Plate_Thickness = Plate_Thickness
            self.Plate_Dimensions = Plate_Dimensions
            self.Plate_Quantity = Plate_Dimensions
            self.Plate_Standard_Weight = Plate_Standard_Weight
        def set_plate_thickness(self,Plate_Thickness):
            self.Plate_Thickness = Plate_Thickness
        def get_plate_thickness(self):
            return self.Plate_Thickness
        def set_plate_dimensions(self,Plate_Dimensions):
            self.Plate_Dimensions = Plate_Dimensions
        def get_plate_dimensions(self):
            return self.Plate_Dimensions
        def set_plate_quantity(self,Plate_Quantity):
            self.Plate_Quantity = Plate_Quantity
        def get_plate_quantity(self):
            return self.Plate_Quantity
        def get_plate_standard_weight(self):
            return self.Plate_Standard_Weight
   
    platedetails = PlateDetails()


    def get_plate_details(plt):
        platedetails = PlateDetails()
        if 'X' in plt:
            plt = plt.replace('X','x')
        if '%' in plt:
            plt = plt.replace('%','x')
        if 'O' in plt:
            plt = plt.replace('O','0')
        if 'o' in plt:
            plt = plt.replace('o','0')
        if 'I' in plt:
            plt = plt.replace('I','1')
        if 'i' in plt:
            plt = plt.replace('i','1')
        if 'l' in plt:
            plt = plt.replace('l','1')
        plt = plt.replace(' ','')
        plt_1 = plt.index("PLT") + 3
        plt_3 = plt.index("THK") + 3
        for i in range(plt_3-3,0,-1):
            if plt[i]=='x':
                plt_2 = i
                break
        platedetails.set_plate_dimensions(plt[plt_1:plt_2])
        platedetails.set_plate_thickness(plt[plt_2+1:plt_3])
        plt_no = plt.index('N0')
        plate_quantity = ''
        for i in range(plt_3,plt_no):
            if plt[i].isnumeric()==True:
                plate_quantity = plate_quantity + plt[i]
        plate_quantity = int(plate_quantity)  
        platedetails.set_plate_quantity(plate_quantity)
        return platedetails


except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
