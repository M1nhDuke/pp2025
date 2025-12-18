class Student:
    def __init__(self, name, id, dob):
        self._name = name
        self._id = id
        self._dob = dob
        self._gpa = 0.0

    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getDob(self):
        return self._dob

    def getGPA(self):
        return self._gpa

    def setGPA(self, g):
        self._gpa = g

    def __str__(self):
        return f"ID: {self._id:<10} | Name: {self._name:<15} | GPA: {self._gpa:.1f}"