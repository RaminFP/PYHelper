# -*- coding: utf-8 -*-
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from db_config.connector import ConnectorDB
from db_config.config import CONNECTOR

metadata = MetaData(ConnectorDB().ConnectMySQL())
Base = declarative_base(metadata=metadata)

'''
    Class :Name : User
    Tabel :Name : tbUser
    Relation    : None
'''

class User(Base):

    __tablename__ = 'tbUser'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    about_me = Column(String(140))
    address = Column(String(150))

if CONNECTOR:
    metadata.create_all(ConnectorDB().ConnectMySQL())


