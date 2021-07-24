#!/usr/bin/python3

import base64

def encode(string):
    string_bytes = string.encode("ascii")
    encoded_bytes = base64.b64encode(string_bytes)
    base64_output_string = encoded_bytes.decode('ascii')
    return base64_output_string
 
if __name__ == "__main__":
    f = open("base-onion.txt", "a")

    encode_string = "NEWBIE{N0_hop3_Ju5t_4dd1ng_l4y3rs}"

    for i in range(36):
        encode_string = encode(encode_string)
    f.write(encode_string)

    f.close()