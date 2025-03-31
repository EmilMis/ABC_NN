from flask import Flask, jsonify, render_template, request
import net
import datetime
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    matrix = data.get('matrix', [])
    data = str(net.e(matrix).tolist())
    return jsonify(message="Matrix received!", time=data)


if __name__ == '__main__':
    app.run(debug=True)
