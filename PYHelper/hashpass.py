# -*- coding: utf-8 -*-
## Password Hasher

from passlib.hash import pbkdf2_sha256


class Hasher(object):

    def CreateHash(self,pPassword):
        try:
            return pbkdf2_sha256.encrypt(pPassword, rounds=200000, salt_size=32)
        except Exception as e:
            raise


    def ValidatePassword(self,pPassword, pHashed):
        try:
            return pbkdf2_sha256.verify(pPassword, pHashed)
        except Exception as e:
            raise