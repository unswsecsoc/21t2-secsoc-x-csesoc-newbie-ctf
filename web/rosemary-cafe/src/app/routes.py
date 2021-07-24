from app import app
from flask import render_template, request

PASSWORD = 'yumyum'

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('login.html', message='')
    else:
        if request.form['password'] == PASSWORD:
            return render_template('dash.html', message='NEWBIE{m4ybE_th3se_#a5#_br0wn5_aR3_beTt3R_s4lTeD}')
        else:
            return render_template('login.html', message='Password does not produce expected SHA256 <kbd>404267835521b93069c5fcde86845534c2f0b03b4d77cb911cd61fc9b84b2082</kbd>')
    
@app.route('/favicon.ico')
def favicon():
    return ''
