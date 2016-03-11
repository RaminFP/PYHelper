# -*- coding: utf-8 -*-
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from db_config.connector import ConnectorDB



metadata = MetaData(ConnectorDB().ConnectMySQL())
Base = declarative_base(metadata=metadata)


class self_reflation(Base):

        __tablename__ = 'tbSelf'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        parent_id = Column(Integer, ForeignKey('tbSelf.id'))
        children = relationship(lambda: self_reflation, remote_side=[id])


metadata.create_all(ConnectorDB().ConnectMySQL())

