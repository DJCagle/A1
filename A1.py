import yaml
import os
import json

from flask import Flask
from flask import render_template

app = Flask(__name__)

for fn in json.glob('data/*.yaml'):
    with open(fn, 'r') as yf:
        play = json.load(yf)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
