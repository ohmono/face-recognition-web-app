from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import uuid
import os
import pickle
import cv2

# loading models
haar = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
# pickle files
mean = pickle.load(open('./models/mean_preprocess.pickle', 'rb'))
model_svm = pickle.load(open('./models/model_svm.pickle', 'rb'))
model_pca = pickle.load(open('./models/pca_50.pickle', 'rb'))

gender_pre = ['Male', 'Female']
font = cv2.FONT_HERSHEY_SIMPLEX

UPLOAD_FOLDER = './img'

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/img/{folder}/{id}")
def home(folder: str, id: str):
    return FileResponse(f'./img/{folder}/{id}')


@app.post("/img/")
def upload(image: UploadFile = File(...)):
    # create new folder per image
    fodler_path = str(uuid.uuid4())
    dir = os.path.join(UPLOAD_FOLDER, fodler_path)
    if not os.path.exists(dir):
        os.mkdir(dir)
    # saving orinigal image
    filename = image.filename
    path = os.path.join(dir, '0_'+filename)
    with open(path, 'wb') as folder:
        folder.write(image.file.read())

    color = 'bgr'
    # step - 1: read image
    img = cv2.imread(path)

    # step - 2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # step - 3: crop the face (using haar cascase classifier)
    faces = haar.detectMultiScale(gray, 1.5, 3)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)  # drawing rectangle
        roi = gray[y:y+h, x:x+w]  # crop image
        # step - 4: normalization (0-1)
        min_val, max_val = roi.min(), roi.max()
        roi = (roi - min_val)/(max_val - min_val)
        # step - 5: resize images (100,100)
        if roi.shape[1] > 100:
            roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_AREA)
        else:
            roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_CUBIC)

        # step - 6: Flattening (1x10000)
        roi_reshape = roi_resize.reshape(1, 10000)  # 1,-1
        # step - 7: subptract with mean
        roi_mean = roi_reshape - mean
        # step - 8: get eigen image
        eigen_image = model_pca.transform(roi_mean)
        # step - 9: pass to ml model (svm)
        results = model_svm.predict_proba(eigen_image)[0]
        # step - 10:
        predict = results.argmax()  # 0 or 1
        score = results[predict]
        # step - 11:
        text = "%s : %0.2f" % (gender_pre[predict], score)
        cv2.putText(img, text, (x, y), font, 1, (0, 255, 0), 3)

    cv2.imwrite('{}/{}'.format(dir, '1_'+filename), img)

    return {'key': fodler_path, 'img': filename}
