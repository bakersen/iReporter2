from flask import Flask, jsonify, request

from model import Incident

app = Flask(__name__)

@app.route('/')
def testing12():
    return 'Flask is working'


if __name__ == '__main__':
    app.run(debug=True)