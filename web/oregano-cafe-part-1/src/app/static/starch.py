'''
homemade hash function, just like the homemade hash browns at our cafe.
'''


def lcg(x):
    '''
    kinda lcg but spicier i guess.
    '''
    a = 69
    c = 420
    m = 2**8    # ensure 8 bit value returned
    return (a*x + c) % m


def hex_to_bitstring(hexstr):
    '''
    given a hexadecimal string, returns the bitstring representation of it.
    i dont even use this idk why this is here but it seems cool.
    '''
    bitstr = bin(int(hexstr, 16))[2:]
    while len(bitstr) % 8 != 0:
        bitstr = '0' + bitstr
    return bitstr


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
