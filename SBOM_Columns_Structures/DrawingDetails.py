class DrawingDetails:
    def __init__(self,Drawing_Number='',Sheet_Number='',Revision_Number=''):
        self.Drawing_Number = Drawing_Number
        self.Sheet_Number = Sheet_Number
        self.Revision_Number = Revision_Number
    def set_Drawing_Number(self,Drawing_Number):
        self.Drawing_Number = Drawing_Number
    def get_Drawing_Number(self):
        return self.Drawing_Number
    def set_Sheet_Number(self,Sheet_Number):
        self.Sheet_Number = Sheet_Number
    def get_Sheet_Number(self):
        return self.Sheet_Number
    def set_Revision_Number(self,Revision_Number):
        self.Revision_Number = Revision_Number
    def get_Revision_Number(self):
        return self.Revision_Number

drawingdetails = DrawingDetails()