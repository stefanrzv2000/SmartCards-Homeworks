from Crypto.PublicKey import RSA
import Crypto.Signature
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

def generate_key():
    return RSA.generate(1024)

def encrypt(msg,pub_key):
    return pub_key.encrypt(msg)

def decrypt(msg,key):
    return key.decrypt(msg)

def sign(msg,key):
    hsh = SHA256.new(msg)
    signer = PKCS115_SigScheme(key)
    signature = signer.sign(hsh)
    return signature

def verify(msg,sig,pub_key):
    hsh = SHA256.new(msg)
    verifier = PKCS115_SigScheme(pub_key)
    try:
        verifier.verify(hsh, sig)
        return True
    except:
        return False