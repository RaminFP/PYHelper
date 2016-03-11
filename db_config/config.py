# -*- coding: utf-8 -*-
'''

    ## Database Connection Information

    :HOST    : your DB ipaddress ,
    :DATABSE : your database name if noe exist database in your db you should create database ans set here,
    :PORT    : database port set here for mysql defualt port : 3306
    :USER    : your username of your databse
    :PASSWORD: your password databse if not set password set ''

'''

MySQL = True
PostgreSQL = False

CONNECTOR = True

class MySQLDB:

    HOST = "127.0.0.1"
    DATABASE = "ser-sqlal"
    PORT = "3306"
    USER = "root"
    PASSWORD = ""


class PostgreSQL:

    HOST = "127.0.0.1"
    DATABASE = "ser-sqlal"
    PORT = "3306"
    USER = "root"
    PASSWORD = ""
