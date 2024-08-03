from flask import Flask, request, jsonify
from flask_cors import CORS
from openaicv import get_image_data
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/classify_image", methods=["POST"])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Path to the directory
    dir_path = './uploads/'

    # Check if the directory exists
    if not os.path.exists(dir_path):
        print("DIR DOES NOT EXIST!")
        os.makedirs(dir_path, exist_ok=True)

    file_location = f'./uploads/{file.filename}'
    file.save(file_location)

    response = get_image_data(file_location)
    return jsonify({'message': response}), 200 

if __name__ == "__main__":
    app.run(debug=True)