from domain.student import Student
from domain.course import Course
from domain.enrollment import Enrollment
from db.models import StudentEntity, CourseEntity, EnrollmentEntity
from db.database import SessionLocal

class IllegalStateException(Exception):
    pass

class StudentService:
    def __init__(self):
        # In Java, these were injected repositories.
        # Here we will just use the session directly for simplicity.
        pass

    def enrollInCourse(self, studentId, courseId):
        # TODO Implement logic
        # A student cannot enroll in the same course more than twice.
        # A student cannot enroll in an advanced course on a specific topic unless they have already completed the corresponding basic courses.
        # Prevent double enrollment in the same course in the same semester.
        # Only existing student can sign up to the existing course
        pass

    def findAll(self):
        session = SessionLocal()
        try:
            entities = session.query(StudentEntity).all()
            return [self.mapToDomain(e) for e in entities]
        finally:
            session.close()

    def findById(self, id):
        session = SessionLocal()
        try:
            entity = session.query(StudentEntity).filter(StudentEntity.id == id).first()
            if entity:
                return self.mapToDomain(entity)
            return None
        finally:
            session.close()

    def deleteById(self, id):
        session = SessionLocal()
        try:
            # Check if enrolled
            exists = session.query(EnrollmentEntity).filter(EnrollmentEntity.student_id == id).first() is not None
            if exists:
                raise IllegalStateException("Cannot delete student who is enrolled in courses")
            student_entity = session.query(StudentEntity).filter(StudentEntity.id == id).first()
            if student_entity:
                session.delete(student_entity)
                session.commit()
        finally:
            session.close()

    def mapToDomain(self, studentEntity):
        enrollments = [self.mapEnrollmentToDomain(e) for e in studentEntity.enrollments]
        return Student(studentEntity.id, studentEntity.name, enrollments)

    def mapCourseToDomain(self, courseEntity):
        return Course(courseEntity.id, courseEntity.title, courseEntity.is_advanced, courseEntity.topic)

    def mapEnrollmentToDomain(self, enrollmentEntity):
        return Enrollment(enrollmentEntity.id, enrollmentEntity.student.id, self.mapCourseToDomain(enrollmentEntity.course))

    def mapStudentToEntity(self, student):
        entity = StudentEntity(name=student.getName())
        return entity

    def mapCourseToEntity(self, course):
        return CourseEntity(title=course.getTitle(), is_advanced=course.isAdvanced(), topic=course.getTopic())
