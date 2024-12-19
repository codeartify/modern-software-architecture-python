import uvicorn
from fastapi import FastAPI
from db.database import Base, engine, SessionLocal
from db.models import CourseEntity, StudentEntity, EnrollmentEntity
from controller.student_controller import router as student_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Insert initial data
db = SessionLocal()
try:
    # Courses
    course1 = CourseEntity(title='Math 101', is_advanced=False, topic='Mathematics')
    course2 = CourseEntity(title='History 101', is_advanced=False, topic='History')
    db.add(course1)
    db.add(course2)
    db.flush()  # get IDs

    # Students
    student1 = StudentEntity(name='John Doe')
    student2 = StudentEntity(name='Jane Smith')
    db.add(student1)
    db.add(student2)
    db.flush()

    # Enrollments
    enrollment1 = EnrollmentEntity(student_id=student1.id, course_id=course1.id)
    enrollment2 = EnrollmentEntity(student_id=student2.id, course_id=course2.id)
    db.add(enrollment1)
    db.add(enrollment2)

    db.commit()
finally:
    db.close()

app.include_router(student_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8765)
