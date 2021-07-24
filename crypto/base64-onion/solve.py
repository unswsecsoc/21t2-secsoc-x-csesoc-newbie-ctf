#!/usr/bin/python3

import base64

def decode(string):
    string_bytes = string.encode("ascii")
    decoded_bytes = base64.b64decode(string_bytes)
    decoded_string = decoded_bytes.decode('ascii')
    return decoded_string

if __name__ == "__main__":
    f = open("base-onion.txt", "r")

    encoded_string = f.read()

    while True:
        try:
            encoded_string = decode(encoded_string)
        except:
            print(encoded_string)
        finally:
            f.close()