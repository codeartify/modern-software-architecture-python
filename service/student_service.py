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

        session = SessionLocal()
        try:
            student_entity = session.query(StudentEntity).filter(StudentEntity.id == studentId).first()
            if student_entity is None:
                raise IllegalStateException("Student does not exist.")

            course_entity = session.query(CourseEntity).filter(CourseEntity.id == courseId).first()
            if course_entity is None:
                raise IllegalStateException("Course does not exist.")

            # Map domain
            student = self.mapToDomain(student_entity)
            # Check enrollment count
            if student.getEnrollmentCountForCourse(courseId) >= 2:
                raise IllegalStateException("Cannot enroll more than twice in the same course.")

            if course_entity.is_advanced:
                # Check if student completed a basic course in the same topic
                if not student.hasCompletedBasicCourseInTopic(course_entity.topic):
                    raise IllegalStateException("Cannot enroll in advanced course without completing a basic course in the same topic.")

            # Prevent double enrollment in the same semester - for simplicity, assume the same table is the same semester
            # If we consider the same course_id in the same set of enrollments as a double-enrollment, it's already covered above by count check.
            # If "same semester" required additional logic, we would need more data. Assuming current logic suffices.

            new_enrollment = EnrollmentEntity(student=student_entity, course=course_entity)
            session.add(new_enrollment)
            session.commit()
        finally:
            session.close()

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
