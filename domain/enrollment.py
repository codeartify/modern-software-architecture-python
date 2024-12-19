class Enrollment:
    def __init__(self, id, studentId, course):
        self._id = id
        self._studentId = studentId
        self._course = course

    def getId(self):
        return self._id

    def getStudentId(self):
        return self._studentId

    def getCourse(self):
        return self._course
