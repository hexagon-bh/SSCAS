from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)

current_index = 0
characters = ['A', 'B', 'C']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_character', methods=['GET'])
def get_character():
    global current_index
    character = characters[current_index]
    current_index = (current_index + 1) % len(characters)
    return jsonify({'character': character})

@app.route('/poll_characters', methods=['GET'])
def poll_characters():
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:  # 10초 동안 폴링을 진행하고 종료합니다.
            break

        time.sleep(1)  # 1초 간격으로 폴링을 수행합니다.

        character = characters[current_index]
        return jsonify({'character': character})

if __name__ == '__main__':
    app.run(debug=True)
