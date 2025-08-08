from flask import Flask, request, jsonify
from main import handle_user_input

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_id = data.get('user_id')
    user_message = data.get('message')

    if not user_id or not user_message:
        return jsonify({'error': 'Missing user_id or message'}), 400

    response = handle_user_input(user_id, user_message)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
