import numpy as np
import logging
from flask import Flask, request, jsonify, render_template
import pickle
import model
app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    #app.run(debug=True)  # running the app