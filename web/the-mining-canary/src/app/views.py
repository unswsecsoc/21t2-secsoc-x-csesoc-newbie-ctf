from flask import request, render_template, send_from_directory
from flask.helpers import make_response
from app import app

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('FLAG (3/3)', '_m0r3}')
    return resp

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
