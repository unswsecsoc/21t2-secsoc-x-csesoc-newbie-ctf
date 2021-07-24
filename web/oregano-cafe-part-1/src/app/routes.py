from app import app
from flask import render_template, request, send_from_directory

PASSWORD_STARCH = 'a4ec243c744c8424fcb454f4cc4464246ca40484243cd454bcf41424fc048c04'

def lcg(x):
    '''
    kinda lcg but spicier i guess.
    '''
    a = 69
    c = 420
    m = 2**8    # ensure 8 bit value returned
    return (a*x + c) % m

def starch(input_string):
    '''
    hash function.
    '''

    # add a bunch of As in case the input isn't long enough (these will get truncated later if not needed anyways)
    input_string += 'A' * 32
    # construct a string of bits
    bitstr = ''
    # pass the ascii value of the first letter to lcg
    last = lcg(ord(input_string[0]))

    # only take the first 32 characters of the input to make the hash shorter. rest are ignored.
    for char in input_string[:32]:
        # get some 8 bit value from lcg
        bits = lcg(ord(char) * last)
        # append it to bitstring
        bitstr += str(bin(bits))[2:].zfill(8)
        # some more randomness, because why not?
        last = lcg(bits)

    # return the bitstring as hexadecimal
    return hex(int(bitstr, 2))[2:]

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('login.html', message='')
    else:
        if starch(request.form['password']) == PASSWORD_STARCH:
            return render_template('dash.html', message='Part 1 Flag: NEWBIE{wriTinG_y0uR_0wn_ha5#_fuNcTi0N_iSnT_th3_b3St_id3A!}')
        else:
            return render_template('login.html', message=f'Password does not produce expected starch hash: <kbd>{PASSWORD_STARCH}</kbd>')
    
@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/starch.py')
def starch_source():
    return send_from_directory(app.static_folder, request.path[1:])
