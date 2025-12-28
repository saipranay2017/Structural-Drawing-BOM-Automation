try:
    class AngleCleatDetails:
        def __init__(self,Angle_Cleat_Section='',Angle_Cleat_Length=0,Angle_Cleat_Quantity=0):
            self.Angle_Cleat_Section = Angle_Cleat_Section
            self.Angle_Cleat_Length  = Angle_Cleat_Length
            self.Angle_Cleat_Quantity = Angle_Cleat_Quantity
        def set_angle_cleat_section(self,Angle_Cleat_Section):
            self.Angle_Cleat_Section = Angle_Cleat_Section
        def get_angle_cleat_section(self):
            return self.Angle_Cleat_Section
        def set_angle_cleat_length(self,Angle_Cleat_Length):
            self.Angle_Cleat_Length = Angle_Cleat_Length
        def get_angle_cleat_length(self):
            return self.Angle_Cleat_Length
        def set_angle_cleat_quantity(self,Angle_Cleat_Quantity):
            self.Angle_Cleat_Quantity = Angle_Cleat_Quantity
        def get_angle_cleat_quantity(self):
            return self.Angle_Cleat_Quantity
   
    def get_angle_cleat_details(isa):
        anglecleatdetails = AngleCleatDetails()
        if 'X' in isa:
            isa = isa.replace('X','x')
        if '%' in isa:
            isa = isa.replace('%','x')
        if 'O' in isa:
            isa = isa.replace('O','0')
        if 'o' in isa:
            isa = isa.replace('o','0')
        if 'i' in isa:
            isa = isa.replace('i','1')
        if 'l' in isa:
            isa = isa.replace('l','1')
        isa_angle = isa.index("ISA")
        isa_thk   = isa.index("THK")
        anglecleatdetails.set_angle_cleat_section(isa[isa_angle:isa_thk])
        isa_thk   = isa_thk + 3
        isa_lg    = isa.index("Lg")
        anglecleatdetails.set_angle_cleat_length(int(isa[isa_thk:isa_lg]))
        isa_no    = isa.index("N0")
        isa_quantity = ''
        if 'I' in isa:
            isa = isa.replace('I','1')
        for i in range(isa_lg,isa_no):
            if isa[i].isnumeric()==True:
                isa_quantity = isa_quantity + isa[i]
        isa_quantity = int(isa_quantity)  
        anglecleatdetails.set_angle_cleat_quantity(isa_quantity)
        return anglecleatdetails
   
except Exception as e:
    print(e)
    print("ERROR OCCURED")
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')
