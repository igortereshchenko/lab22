from sqlalchemy import Column, String, Integer, Date

from LecturebotDAL.dbcontext import ModelBase


class Teacher(ModelBase):
    __tablename__ = 'Teacher'

    Id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Birthday = Column(Integer, nullable=False)
    Salary = Column(Integer, nullable=False)
    Position = Column(String, nullable=False)

    def __init__(self, name, birthday, salary, position):
        self.Name = name
        self.Birthday = birthday
        self.Salary = salary
        self.Position = position
