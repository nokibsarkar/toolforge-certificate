import os
from os.path import join, dirname
from flask import Flask, render_template, request, redirect, url_for, session
from oauth import oauth
import json
__dir__ = dirname(__file__)
app = Flask(
    __name__,
    template_folder = join(__dir__, 'templates'),
    static_folder= join(__dir__, 'static'),
    static_url_path='/static'
)

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
    user = {
        'bn_name' : 'Nokib',
        'certificates' : [],
        'workshops' : []
    }
    return render_template('index.jinja', user= user)

if __name__ == '__main__':
    app.run(debug=True)