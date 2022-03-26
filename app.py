import os
from os.path import join, dirname
os.system("pip install -r requirements.txt")
from flask import Flask, render_template, request, redirect, url_for, session
from oauth import oauth
import json
app = Flask(__name__)
__dir__ = dirname(__file__)
with open(join(__dir__, 'config.json'), "r") as f:
    app.config.update(json.load(f))


##########################
# Mediawiki OAuth setup
##########################

app.register_blueprint(oauth, url_prefix='/')
@app.post('/integrate')
def integrate():
    os.system('git pull && webservice stop && webservice python3.7 start')
    return 'OK'

@app.get("/")
def index():
    return "Okay"

if __name__ == '__main__':
    app.run(debug=True)