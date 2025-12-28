class ExcelRows:
    def __init__(self,current_row=6,pivot_row=6,workbooks=None,workbook_flag=0):
        self.current_row = current_row
        self.pivot_row = pivot_row
        self.workbooks = workbooks
        self.workbook_flag = workbook_flag
    def set_current_row(self,current_row):
        self.current_row = current_row
    def get_current_row(self):
        return self.current_row
    def set_pivot_row(self,pivot_row):
        self.pivot_row = pivot_row
    def get_pivot_row(self):
        return self.pivot_row
    def set_workbooks(self,workbooks):
        self.workbooks=workbooks
    def get_workbooks(self):
        return self.workbooks
    def set_workbook_flag(self,workbook_flag):
        self.workbook_flag=workbook_flag
    def get_workbook_flag(self):
        return self.workbook_flag
    
excelrows = ExcelRows()