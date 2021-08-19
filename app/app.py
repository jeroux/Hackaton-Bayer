import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__)
model = tf.keras.models.load_model("plant_disease")


@app.route("/")
def home():
    return render_template("index.html")


UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        print(request.files)
        print(request.form)
        if 'filename' not in request.files:
            return 'there is no filename in form!'
        file1 = request.files['filename']
        print(file1.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return model_predict(file1.filename)

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="filename">
      <input type="submit">
    </form>
    '''


CATEGORIES =['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
             'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
             'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
             'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
             'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
             'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
             'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
             'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
             'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
             'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
             'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
             'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']


def prepare(filepath):
    IMG_SIZE = 224
    img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE),3)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


def model_predict(filename):
    prediction = model.predict([prepare(f"{os.getcwd()}/upload/{filename}")])
    return str(CATEGORIES[(np.argmax(prediction))])


if __name__ == "__main__":
    app.run(debug=True)
