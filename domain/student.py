class Student:
    def __init__(self, id, name, enrollments):
        self._id = id
        self._name = name
        self._enrollments = enrollments

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getEnrollments(self):
        return self._enrollments

    def hasCompletedBasicCourseInTopic(self, topic):
        return any(e.getCourse().getTopic() == topic and not e.getCourse().isAdvanced() for e in self._enrollments)

    def getEnrollmentCountForCourse(self, courseId):
        return sum(1 for e in self._enrollments if e.getCourse().getId() == courseId)
