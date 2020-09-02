"""
This module defines what will happen in stage-3.
"""
from flask import Flask, make_request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return make_request(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
