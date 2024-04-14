import subprocess
import os
from flask import Flask, request, jsonify

from demo.detector import ResNetDetector

def predict_video(video_path):
    cfg = f"configs/test.yml"
    detector = ResNetDetector("resnet",cfg)
    x = detector.predict(open(video_path, "rb").read())
    if not len(x.iloc[0]["predict"]):
        return False
    scores = [item["score"] for item in x.iloc[0]["predict"]]
    return (sum(scores) / len(scores)) > 0.9

def images_to_video(image_path, video_name):
    # ffmpeg -f image2 -framerate 25 -i {image_path} {video_name}
    subprocess.run(f"ffmpeg -f image2 -framerate 25 -i {image_path} {video_name} -y", shell=True)

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

UPLOAD_FOLDER = 'temp'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    
    images_to_video(filename, "temp/video.mp4")
    res = predict_video("temp/video.mp4")
    print("res:", res)
    
    return jsonify({'valid': res}), 200

@app.route('/upload-video', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    
    res = predict_video(filename)
    print("res:", res)
    
    return jsonify({'valid': res}), 200

if __name__ == "__main__":
    # video_path = "../face-spoofing-dection-ABFTSCNN/data_extract/demo/video.mp4"
    # predict_video(video_path)

    # images_to_video("temp/dichlenhietba.webp", "temp/dichlenhietba.mp4")
    # print(predict_video("temp/dichlenhietba.mp4"))
    
    app.run(debug=True, host='0.0.0.0', port=20627)
    
    