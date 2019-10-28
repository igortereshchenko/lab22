from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from LecturebotDAL import dbconnection

connection_string = 'postgres://vrmxzzljygpurv:cd8e1a3b1a7aa3e6fff96c30465d20693268069267dd9fcfc10c8699d1c082d0@ec2-54-83-202-132.compute-1.amazonaws.com:5432/d3g0he26mjd1be'

DBEngine = create_engine(connection_string)
Session = sessionmaker(bind=DBEngine)

ModelBase = declarative_base()
session = Session()
