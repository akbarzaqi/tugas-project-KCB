from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np

app = Flask(__name__)

cam = cv2.VideoCapture(0)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])



def generate_frames():
    global isBlueDetected, isRedDetected
    global countRed, countBlue
    while True:
        success, img = cam.read()
        if not success:
            break
        
        isBlueDetected = False
        isRedDetected = False
        countRed = 0
        countBlue = 0

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        maskRed = cv2.inRange(hsv, lower_red, upper_red)
        maskBlue = cv2.inRange(hsv, lower_blue, upper_blue)

        redContours, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blueContours, _ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
       
        for contour in redContours:
            if cv2.contourArea(contour) > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(img, "merah", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
                isRedDetected = True
                countRed += 1

      
        for contour in blueContours:
            if cv2.contourArea(contour) > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(img, "biru", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)
                isBlueDetected = True
                countBlue += 1

        
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/status')
def status():
    print("cek status : merah : ", isRedDetected, "biru : ", isBlueDetected)
    return jsonify({
        "countBlue" : countBlue,
        "countRed" : countRed,
        "red": isRedDetected,
        "blue": isBlueDetected
    })

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=8888)
