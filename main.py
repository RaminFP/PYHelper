from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from db_config.connector import ConnectorDB
from sqla_model.Users import User
from sqla_model.Users import Base


session = scoped_session(sessionmaker(bind=ConnectorDB().ConnectMySQL()))
Base.query = session.query_property()



def AddUsers():


    user1 = User(name="ramin",email="ramin.blackhat@gmail.com",about_me="i am programmer",address="babol")
    user2 = User(name="reza",email="ramin.black@gmail.com",about_me="i am programmer",address="babol")
    user3 = User(name="mehdi",email="ramin.hat@gmail.com",about_me="i am programmer",address="babol")
    session.add_all([user1,user2,user3])
    session.commit()

def JsonUser():

    from sqla_serializer.serializer import UserSchema
    UserSerializer = UserSchema()
    jsonusers = session.query(User)
    data,error = UserSerializer.dump(jsonusers,many=True)
    if error:
        print "you get error : %s " % error
    else:
        for item in data:
            print item


def main():

    JsonUser()
    #AddUsers()




if __name__ == '__main__':
   main()

