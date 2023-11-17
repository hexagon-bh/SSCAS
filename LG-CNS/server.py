from flask import Flask, render_template, Response, send_file, jsonify
import cv2
import time
import numpy as np
from roboflow import Roboflow
import socket
import os
from _thread import *
import shutil

HOST = '192.168.144.247' ## server에 출력되는 ip를 입력해주세요 ##
PORT = 9999

app = Flask(__name__)
camera = cv2.VideoCapture("http://192.168.144.241:81/stream") # 0은 기본 카메라를 나타냅니다. 만약 다른 카메라를 사용하려면 해당 인덱스를 사용하세요.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
ok=0
analysis_data=[]

def recv_data(client_socket):
    global analysis_data,ok
    while True:
        data = client_socket.recv(1024)
        analysis_data=list(data.decode().split(":"))
        if analysis_data[0]=="analysis":
            print("recive : ", repr(data.decode()))
            ok=1

start_new_thread(recv_data, (client_socket,))
print('>> Connect Server')

def generate_frames():
    global client_socket,ok
    while True:
        cnt=0
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # 5초마다 한 번씩 카메라 프레임 저장
            if int(time.time()) % 5 == 0:
                # 인코딩된 프레임을 NumPy 배열로 디코딩
                frame_array = np.frombuffer(frame, dtype=np.uint8)
                # NumPy 배열을 이미지로 디코딩
                img = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
                # 프레임을 저장
                cv2.imwrite(f'static/assets/img/pre_picture.jpg', img)
                if (cnt!=0 and ok==1) or cnt==0:
                    message="recog"
                    client_socket.send(message.encode())
                    cnt+=1
                    ok=0

@app.route('/')
def index():
    source_path = 'static/assets/img/white.jpg'
    destination_path = 'static/assets/img/saved_picture.jpg'
    shutil.copy(source_path, destination_path)
    destination_path = 'static/assets/img/heatmap.jpg'
    shutil.copy(source_path, destination_path)
    print('이미지가 성공적으로 복사되었습니다.')
    return render_template('index.html')


@app.route('/concert')
def concert():
    return render_template('concert.html')

@app.route('/path')
def path():
    return render_template('path.html')

@app.route('/get_image/<string:no>')
def get_image(no):
    # 이미지를 생성하거나 가져오는 로직을 추가합니다.
    # 여기에서는 단순히 예시로 사용되는 이미지를 반환합니다.
    if no=="1":
        image_path = 'static/assets/img/saved_picture.jpg'
    elif no=="2":
        image_path = 'static/assets/img/heatmap.jpg'
    return send_file(image_path, mimetype='image/jpg')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_character', methods=['GET'])
def get_character():
    global analysis_data
    if len(analysis_data)==5:
        analysis_data[3]=analysis_data[3].replace("'",":")
        j_data={'place': analysis_data[4],'time': analysis_data[3],'person':analysis_data[2],'density': analysis_data[1]}
    else:
        j_data={'place': "",'time': "",'person':"",'density': ""}
    return jsonify(j_data)

@app.route('/poll_characters', methods=['GET'])
def poll_characters():
    global analysis_data
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:  # 10초 동안 폴링을 진행하고 종료합니다.
            break

        time.sleep(1)  # 1초 간격으로 폴링을 수행합니다.
        if len(analysis_data)==5:
            j_data={'place': analysis_data[4],'time': analysis_data[3],'person':analysis_data[2],'density': analysis_data[1]}
        else:
            j_data={'place': "",'time': "",'person':"",'density': ""}
        return jsonify(j_data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
client_socket.close()