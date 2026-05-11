from flask import Flask, render_template, request, jsonify
import rsa
import json
import os

app = Flask(__name__)
DB_FILE = 'chat_db.json'

def init_db():
    # Khởi tạo database mới mỗi lần chạy để tránh rác dữ liệu
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump({"users": {}, "messages": []}, f, ensure_ascii=False, indent=4)

def get_db():
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    db = get_db()
    # Lưu Public Key của user
    db['users'][data['username']] = data['public_key']
    save_db(db)
    return jsonify({"status": "CONNECTED"})

@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    return jsonify(db['users'])

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    db = get_db()
    db['messages'].append({
        "to": data['to'],
        "ciphertext": data['ciphertext']
    })
    save_db(db)
    return jsonify({"status": "TRANSMITTED"})

@app.route('/receive/<username>', methods=['GET'])
def receive_messages(username):
    db = get_db()
    # Lấy tin nhắn dành cho username này
    my_msgs = [m for m in db['messages'] if m['to'] == username]
    return jsonify(my_msgs)

if __name__ == '__main__':
    init_db()
    print(f"--- SERVER DNU RSA ĐANG CHẠY TẠI: http://172.16.67.198:5000 ---")
    # Quan trọng: host='0.0.0.0' để máy bạn bạn truy cập được
    app.run(host='0.0.0.0', port=5000, debug=True)