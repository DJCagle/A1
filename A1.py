import os
import yaml
import glob

from flask import Flask
from flask import render_template

# create global plays dictionary
plays = {}
# loop over the files
for fn in glob.glob('data/*.yaml'):
    # load data from fn and put in dictionary
    with open(fn, 'r') as yf:
        play = yaml.load(yf)
        plays[play['id']] = play


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', plays=plays)


if __name__ == '__main__':
    app.run()
