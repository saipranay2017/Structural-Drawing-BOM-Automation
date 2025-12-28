try:
    import glob
    import os
    import traceback
   
    def find_pdf_files(directory):
        pdf_files = glob.glob(os.path.join(directory, '*.pdf'))
        pdf_file_names = [os.path.basename(file) for file in pdf_files]
        return pdf_file_names
   
    def find_png_files(directory):
        png_files = glob.glob(os.path.join(directory, '*.png'))
        png_file_names = [os.path.basename(file) for file in png_files]
        return png_file_names
   
    def find_excel_files(directory):
        excel_files = glob.glob(os.path.join(directory, '*.xlsx'))
        excel_file_names = [os.path.basename(file) for file in excel_files]
        return excel_file_names
   
    directory_path = './static'
   
    def remove_files():
        pdf_files = find_pdf_files(directory_path)
        for pdf in pdf_files:
            os.remove(f'static/{pdf}')
   
   
        excel_files = find_excel_files(directory_path)
        for excel in excel_files:
            os.remove(f'static/{excel}')
   
   
        png_files = find_png_files(directory_path)
        for png in png_files:
            os.remove(f'static/{png}')


except:
    traceback.print_exc()
    