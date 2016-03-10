from sqlalchemy import create_engine
from db_config.config import MySQLDB
from db_config.config import PostgreSQL

class ConnectorDB():

    def ConnectMySQL(self):

            con = 'mysql://{}:{}@{}:{}/{}'.format(MySQLDB().USER,MySQLDB().PASSWORD,MySQLDB().HOST,MySQLDB().PORT,MySQLDB().DATABASE)
            self.engine = create_engine(con, echo=True)
            return self.engine

    def ConnectPostgreSQL(self):

            con = 'postgresql://{}:{}@{}:{}/{}'.format(PostgreSQL().USER,PostgreSQL().PASSWORD,PostgreSQL().HOST,PostgreSQL().PORT,PostgreSQL().DATABASE)
            self.engine = create_engine(con, echo=True)
            return  self.engine

    def ConnectSqlite(self):

            self.engine = create_engine('/serializer_sqlalchemy/foo.db', echo=True)
            return  self.engine
