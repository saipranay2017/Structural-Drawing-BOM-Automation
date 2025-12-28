try:
    from openpyxl import load_workbook
   
    book = load_workbook("data.xlsx")
    sheet2 = book.worksheets[1]
   
    class BeamDetails:
        def __init__(self,Beam_Section='',Beam_Length=0,Beam_Quantity=0):
            self.Beam_Section = Beam_Section
            self.Beam_Length = Beam_Length
            self.Beam_Quantity = Beam_Quantity
        def set_beam_section(self,Beam_Section):
            self.Beam_Section = Beam_Section
        def get_beam_section(self,):
            return self.Beam_Section
        def set_beam_length(self,Beam_Length):
            self.Beam_Length = Beam_Length
        def get_beam_length(self):
            return self.Beam_Length
        def set_beam_quantity(self,Beam_Quantity):
            self.Beam_Quantity = Beam_Quantity
        def get_beam_quantity(self):
            return self.Beam_Quantity
   
    def find_beam_in_excel(ism):
        for i in range(1,17):
            if ism == sheet2['A'+str(i)].value:
                return i
        return 0
   
    def find_channel_in_excel(ism):
        for i in range(1,14):
            if ism == sheet2['C'+str(i)].value:
                return i
        return 0
   
    def get_ism_details(ism):
        beamdetails = BeamDetails()
        if 'O' in ism:
            ism = ism.replace('O','0')
        if 'o' in ism:
            ism = ism.replace('o','0')
        ism = ism.replace(' ','')
        if "ISMB" in ism:
            ind1 = ism.index("ISMB")
        elif "ISMC" in ism:
            ind1 = ism.index("ISMC")
        ind2 = ind1 + 4
        while ism[ind2].isnumeric()==True:
            ind2 = ind2 + 1
            if "ISMB" in ism:
                column = find_beam_in_excel(ism[ind1:ind2])
            elif "ISMC" in ism:
                column = find_channel_in_excel(ism[ind1:ind2])
            if column != 0:
                break
        if ism[ind2]=='X' or ism[ind2]=='x':
            ind3 = ind2 + 1
        else:
            ind3 = ind2
        ind3 = ind2 + 1
        while ism[ind3].isnumeric()==True:
            ind3 = ind3 + 1
        beamdetails.set_beam_section(ism[ind1:ind2])
        beamdetails.set_beam_length(int(ism[ind2 + 1 : ind3]))
        if "N0" in ism:
            ind_no = ism.index("N0")
            ind_no = ind_no - 1
            if ism[ind_no] == "I" or ism[ind_no] == "l":
                beamdetails.set_beam_quantity(1)
            else:
                beamdetails.set_beam_quantity(int(ism[ind_no]))
        else:
            beamdetails.set_beam_quantity(1)   
        return beamdetails


except Exception as e:
    print("ERROR OCCURED")
    print(e)
    file = open("FileName.txt","r")
    name = file.readline()
    file.close()        
    os.remove(name+'.png')