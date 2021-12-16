from flask import Flask, jsonify, request
import yes_please

app = Flask(__name__)

@app.route("/encrypt", methods=['POST'])
def get_string():
    request_data = request.get_json()

    if request_data:
        if 'text' in request_data:
            text = request_data["text"]
            return {'text': yes_please.encrypt_string_to_string(text)}
        else:
            return {'error': 'invalid request'}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
