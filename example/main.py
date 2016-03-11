# -*- coding: utf-8 -*-
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from db_config.connector import ConnectorDB
from sqla_model.users import User
from sqla_model.users import Base
from sqla_model.self_relationship import self_reflation

session = scoped_session(sessionmaker(bind=ConnectorDB().ConnectMySQL()))
Base.query = session.query_property()



def AddUsers():

    user1 = User(name="ramin",email="ramin.blackhat@gmail.com",about_me="i am programmer",address="babol")
    user2 = User(name="reza",email="ramin.black@gmail.com",about_me="i am programmer",address="babol")
    user3 = User(name="mehdi",email="ramin.hat@gmail.com",about_me="i am programmer",address="babol")
    session.add_all([user1,user2,user3])
    session.commit()

def Addrelation():

    u1 = self_reflation(name="ramin",parent_id=1)
    session.add_all([u1])
    session.commit()

def Serilizerrelation():

    from sqla_serializer.relationship_serializer import RelationshipSchema
    UserSerializer = RelationshipSchema()
    jsonusers = session.query(self_reflation)
    data,error = UserSerializer.dump(jsonusers,many=True)
    if error:
        print "you get error : %s " % error
    else:

        print data
        from marshmallow_sqlalchemy.fields import get_primary_keys
        prim_key =  get_primary_keys(User)
        print prim_key

def JsonUser():

    from sqla_serializer.serializer import UserSchema
    UserSerializer = UserSchema()
    jsonusers = session.query(User[0])
    data,error = UserSerializer.dump(jsonusers,many=True).data



    if error:
        print "you get error : %s " % error
    else:

        print data
        from marshmallow_sqlalchemy.fields import get_primary_keys
        prim_key =  get_primary_keys(User)
        print prim_key

def main():

    #JsonUser()
    #AddUsers()
    #Addrelation()
    Serilizerrelation()


if __name__ == '__main__':
   main()

