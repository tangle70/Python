#!/bin/env python
###################################################################################
#
#  A script to encode/decode a string using AES 256.
#
###################################################################################

from Crypto.Cipher import AES
import hashlib
import base64
import os
import time

initkey = "tR3QUp$e!E$u4echasweFR?DRUwr57wA"
data = "This is a string. "

# create a cipher object using the random secret
key = hashlib.sha256(initkey).digest() 

def encStr(key, data):
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(key)
    encoded = EncodeAES(cipher, data)
    return encoded

def decStr(key, data):
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(key)
    data = DecodeAES(cipher, data)
    return data

c = 0
x = time.clock()

while c < 1:
    encoded = encStr(key, data)
    print encoded
    decoded = decStr(key, encoded)
    print decoded
    c = c + 1
     
y = time.clock()

print (y - x)
