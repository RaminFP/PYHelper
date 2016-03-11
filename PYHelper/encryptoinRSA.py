# -*- coding: utf-8 -*-


def generate_RSA(bits=2048):
    try:
        '''
        Generate an RSA keypair with an exponent of 65537 in PEM format
        param: bits The key length in bits
        Return private key and public key
        '''
        from Crypto.PublicKey import RSA

        new_key = RSA.generate(bits, e=65537)
        public_key = new_key.publickey().exportKey("PEM")
        private_key = new_key.exportKey("PEM")
        return private_key, public_key
    except Exception as e:
        raise


def decrypt_RSA(private_key, package):
    try:
        '''
        param: public_key_loc Path to your private key
        param: package String to be decrypted
        return decrypted string
        '''
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP
        from base64 import b64decode

        key = private_key
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        str = package.replace(" ", "+")
        decrypted = rsakey.decrypt(b64decode(str))
        return decrypted
    except Exception as e:
        raise


def encrypt_RSA(public_key, message):
    try:
        '''
        param: public_key_loc Path to public key
        param: message String to be encrypted
        return base64 encoded encrypted string
        '''
        from Crypto.PublicKey import RSA
        from Crypto.Cipher import PKCS1_OAEP

        key = public_key
        rsakey = RSA.importKey(key)
        rsakey = PKCS1_OAEP.new(rsakey)
        encrypted = rsakey.encrypt(message)
        return encrypted.encode('base64')
    except Exception as e:
        raise
