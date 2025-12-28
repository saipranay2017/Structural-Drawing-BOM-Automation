from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import glob
import RemoveFiles
from pdftopng_multiple import pdf_to_png
import time

RemoveFiles.remove_files()

app = Flask(__name__)

UPLOAD_FOLDER = './static'
app.secret_key = "Cairocoders-Ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['pdf', 'png'])
directory = './static/'

def find_pdf_files(directory):
    pdf_files = glob.glob(os.path.join(directory, '*.pdf'))
    return [os.path.basename(file) for file in pdf_files]


def find_excel_files(directory):
    excel_files = glob.glob(os.path.join(directory, '*.xlsx'))
    return [os.path.basename(file) for file in excel_files]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_files = []
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request', 'no_files_uploaded': True}), 400


    files = request.files.getlist('files[]')
    if not files or len([f for f in files if f.filename]) == 0:
        return jsonify({'error': 'No files uploaded', 'no_files_uploaded': True}), 400

    RemoveFiles.remove_files()
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_files.append(filename)
    return jsonify({'uploaded_files': uploaded_files, 'no_files_uploaded': False})


@app.route('/process', methods=['POST'])
def process_files():
    directory_path = './static/'
    pdf_files = find_pdf_files(directory_path)
    processed_files = []
    error_pdf_files = []


    for pdf in pdf_files:
        returned = pdf_to_png(pdf)
        if returned == 1:
            print("Success")
        else:
            print("Returned in process_files: ", returned)
            static_index = returned.index("static/")
            static_index = static_index + 7
            error_pdf_files.append(returned[static_index:])
        file = open("FileName.txt","r")
        name = file.readline()
        file.close()
        if os.path.isfile('./static/'+name+'.pdf'):
            os.remove("./static/" + pdf)

    processed_files = find_excel_files(directory_path)

    RemoveFiles.remove_files()
    return jsonify({
        'message': 'Processing completed',
        'processed_files': processed_files,
        'error_pdf_files': error_pdf_files
    })


if __name__ == '__main__':
    app.run(debug=True)

RemoveFiles.remove_files()