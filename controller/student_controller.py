from fastapi import APIRouter, HTTPException, Query
from service.student_service import StudentService, IllegalStateException

router = APIRouter()

service = StudentService()

@router.get("/students")
def getAllStudents():
    students = service.findAll()
    # Return as JSON. We'll convert domain objects to dicts.
    return [
        {
            "id": s.getId(),
            "name": s.getName(),
            "enrollments": [
                {
                    "id": e.getId(),
                    "studentId": e.getStudentId(),
                    "course": {
                        "id": e.getCourse().getId(),
                        "title": e.getCourse().getTitle(),
                        "isAdvanced": e.getCourse().isAdvanced(),
                        "topic": e.getCourse().getTopic()
                    }
                } for e in s.getEnrollments()
            ]
        } for s in students
    ]


@router.get("/students/{id}")
def getStudentById(id: int):
    student = service.findById(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {
        "id": student.getId(),
        "name": student.getName(),
        "enrollments": [
            {
                "id": e.getId(),
                "studentId": e.getStudentId(),
                "course": {
                    "id": e.getCourse().getId(),
                    "title": e.getCourse().getTitle(),
                    "isAdvanced": e.getCourse().isAdvanced(),
                    "topic": e.getCourse().getTopic()
                }
            } for e in student.getEnrollments()
        ]
    }


@router.post("/students/enroll")
def enrollInCourse(studentId: int = Query(...), courseId: int = Query(...)):
    try:
        service.enrollInCourse(studentId, courseId)
        return {"status": "ok"}
    except IllegalStateException as e:
        raise HTTPException(status_code=400, detail=str(e))
