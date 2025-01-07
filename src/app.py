from flask import Flask, Response, render_template
import cv2
from camera import Camera

app = Flask(__name__)

# Initialize the camera (0 is the default camera index)
camera_feed = Camera() 

@app.route('/video_feed')
def video_feed():
    # Return the video stream response
    return Response(camera_feed.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)