from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'feedback.json')

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, 'r') as f:
        return json.load(f)

def save_feedback(feedback_list):
    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedback_list, f, indent=2)

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    data = request.json
    if not data or 'AOI_ID' not in data or 'notes' not in data:
        return jsonify({'error': 'Missing AOI_ID or notes'}), 400
    feedback_list = load_feedback()
    feedback_list.append({
        'AOI_ID': data['AOI_ID'],
        'notes': data['notes'],
        'timestamp': data.get('timestamp')
    })
    save_feedback(feedback_list)
    return jsonify({'status': 'success'}), 201

@app.route('/feedback', methods=['GET'])
def list_feedback():
    return jsonify(load_feedback()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
