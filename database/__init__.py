from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flaskext.mysql import MySQL
from app import app


Base = declarative_base()

DB_FILE = 'sql:///todo_operations.sql'



mysql = MySQL()

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'vivek'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)


    def __init__(self, name, title):
        self.name = name
        self.title = title
