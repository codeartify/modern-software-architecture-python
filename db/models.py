from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .database import Base

class StudentEntity(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    enrollments = relationship("EnrollmentEntity", back_populates="student", cascade="all, delete-orphan")

    def addEnrollment(self, enrollment):
        self.enrollments.append(enrollment)
        enrollment.student = self

    def removeEnrollment(self, enrollment):
        self.enrollments.remove(enrollment)
        enrollment.student = None

class CourseEntity(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    is_advanced = Column(Boolean, nullable=False)
    topic = Column(String(255), nullable=False)
    enrollments = relationship("EnrollmentEntity", back_populates="course", cascade="all, delete-orphan")

    def addEnrollment(self, enrollment):
        self.enrollments.append(enrollment)
        enrollment.course = self

    def removeEnrollment(self, enrollment):
        self.enrollments.remove(enrollment)
        enrollment.course = None

class EnrollmentEntity(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

    student = relationship("StudentEntity", back_populates="enrollments")
    course = relationship("CourseEntity", back_populates="enrollments")
