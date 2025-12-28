class ColumnDetails:
    def __init__(self,description='',section='',length=0,quantity=0):
        self.description = description
        self.section = section
        self.length = length
        self.quantity = quantity
    def set_description(self,description):
        self.description = description
    def get_description(self):
        return self.description
    def set_section(self,section):
        self.section = section
    def get_section(self):
        return self.section
    def set_length(self,length):
        self.length = length
    def get_length(self):
        return self.length
    def set_quantity(self,quantity):
        self.quantity = quantity
    def get_quantity(self):
        return self.quantity
