"""
This module defines what will happen in stage-3.
"""
import os
import sys
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/v2/predict', methods=['GET', 'POST'])
def predict():
    return make_response(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    try:
        username = os.environ['USERNAME']
        password = os.environ['PASSWORD']
        print(f'username: {username}')
        print(f'password: {password}')

        app.run(host='0.0.0.0', port=5000)
    except KeyError as e:
        print(f'cannot find environment variable {e}')
        sys.exit(1)
