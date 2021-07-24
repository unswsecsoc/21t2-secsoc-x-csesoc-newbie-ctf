from app import app
from flask import render_template, request, make_response, redirect
import jwt

USERNAME = 'employee1'
PASSWORD = 'i-work-at-the-most-secure-cafe-ever'

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        if 'auth' in request.cookies and 'is_admin' in jwt.decode(request.cookies.get('auth'), algorithms=None, verify=False):
            if jwt.decode(request.cookies.get('auth'), algorithms=None, verify=False)['is_admin']:
                return render_template('dash.html', message='NEWBIE{w3_l0vE_ch4rGinG_eXCessIve_@mOun+s_&_spEndiNg_N0ne_0n_s3cuRitY}')
            elif jwt.decode(request.cookies.get('auth'), algorithms=None, verify=False)['is_admin'] == False:
                return render_template('dash.html', message='Welcome! You\'re not an admin :(')
        else:
            return render_template('login.html', message='')
    else:
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            resp = make_response(redirect('/'))
            resp.set_cookie('auth', jwt.encode({'username': USERNAME, 'is_admin': False}, key=None, algorithm=None).decode('utf-8'))
            return resp
        else:
            return render_template('login.html', message='Incorrect username or password.')
    
@app.route('/favicon.ico')
def favicon():
    return ''
