class Course:
    def __init__(self, id, title, isAdvanced, topic):
        self._id = id
        self._title = title
        self._isAdvanced = isAdvanced
        self._topic = topic

    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def isAdvanced(self):
        return self._isAdvanced

    def getTopic(self):
        return self._topic
