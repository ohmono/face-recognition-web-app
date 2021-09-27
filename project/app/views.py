from flask import render_template, request, redirect, url_for
import os
from app.utils import pipeline_model
UPLOAD_FOLDER = 'static/uploads'


def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def faceapp():
    return render_template('faceapp.html')


def gender():
    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        # prediction // pipeline model
        pipeline_model(filename, path)
        return render_template('gender.html', fileupload=True, img_name=filename)
    return render_template('gender.html', fileupload=False, img_name=None)