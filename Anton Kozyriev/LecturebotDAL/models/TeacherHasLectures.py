from sqlalchemy import Column, Integer, ForeignKey

from LecturebotDAL.dbcontext import ModelBase


class TeacherHasLectures(ModelBase):
    __tablename__ = 'TeacherHasLectures'

    TeacherId = Column(Integer, ForeignKey('Teacher.Id'), primary_key=True)
    LectureId = Column(Integer, ForeignKey('Lecture.Id'), primary_key=True)

    def __init__(self, teacherid, lectureid):
        self.TeacherId = teacherid
        self.LectureId = lectureid
