from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_config.config import MySQLDB


class ConnectorDB():

    def ConnectMySQL(self):

            con = 'mysql://{}:{}@{}:{}/{}'.format(MySQLDB().USER,MySQLDB().PASSWORD,MySQLDB().HOST,MySQLDB().PORT,MySQLDB().DATABASE)
            self.engine = create_engine(con, echo=True)
            return self.engine

    def ConnectPostgreSQL(self):

            self.engine = create_engine('postgresql://%s:%s@%s/%s', echo=True)
            return  self.engine

    def ConnectSqlite(self):

            self.engine = create_engine('/serializer_sqlalchemy/foo.db', echo=True)
            return  self.engine
