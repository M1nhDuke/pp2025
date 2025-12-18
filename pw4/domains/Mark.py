class Mark:
    def __init__(self, student, mark):
        self._student = student
        self._mark = mark

    def getStudent(self):
        return self._student

    def getMark(self):
        return self._mark