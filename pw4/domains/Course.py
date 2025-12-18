class Course:
    def __init__(self, course_name, course_id, credits):
        self._course_name = course_name
        self._course_id = course_id
        self._credits = credits

    def getCourseName(self):
        return self._course_name

    def getCourseId(self):
        return self._course_id

    def getCredits(self):
        return self._credits

    def info(self):
        print(f"Course ID: {self._course_id}, Course Name: {self._course_name}, Credits: {self._credits}")