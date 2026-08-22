from flask import Flask, request, jsonify
import cv2
import numpy as np
import time
from

02
_plate_recognition
import recognize_plate

app = Flask(__name__)


@app.route("/api/recognize", methods=["POST"])
def recognize():
    start = time.time()
    file = request.files["image"]
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    result = recognize_plate(img)
    process_ms = int((time.time() - start) * 1000)

    return jsonify({
        "code": 200,
        "plate_number": result,
        "process_time_ms": process_ms
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    print("车牌识别服务启动，端口8080")
