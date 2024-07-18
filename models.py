from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from database.database import engine

Base = declarative_base()


class SubjectsModel(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class ClassModel(Base):
    __tablename__ = "class"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class StudentDetailsModel(Base):
    __tablename__ = "student_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String)
    l_name = Column(String)
    password = Column(String)
    email = Column(String)
    class_id = Column(Integer, ForeignKey(ClassModel.id))
    class_relation = relationship(ClassModel, foreign_keys=[class_id])


class StudentSubjectModel(Base):
    __tablename__ = "student_subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer)
    subject_id = Column(Integer, ForeignKey(SubjectsModel.id))
    subject = relationship(SubjectsModel, foreign_keys=[subject_id])


Base.metadata.create_all(engine)
