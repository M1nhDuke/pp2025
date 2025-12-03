# Student Mark Management System using OOP

class Student:
    def __init__(self, name, id, dob):
        self._name = name
        self._id = id
        self._dob = dob

    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getDob(self):
        return self._dob

    def info(self):
        print(f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}")


class Course:
    def __init__(self, course_name, course_id):
        self._course_name = course_name
        self._course_id = course_id

    def getCourseName(self):
        return self._course_name

    def getCourseId(self):
        return self._course_id

    def info(self):
        print(f"Course ID: {self._course_id}, Course Name: {self._course_name}")


class Mark:
    def __init__(self, student, mark):
        self._student = student
        self._mark = mark

    def getStudent(self):
        return self._student

    def getMark(self):
        return self._mark


class USA_shooting_area: # which is school :))))
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def inputStudents(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            name = input("Student Name: ")
            id = input("Student ID: ")
            dob = input("Student DOB: ")
            self.students.append(Student(name, id, dob))

    def inputCourses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            course_name = input("Course Name: ")
            course_id = input("Course ID: ")
            self.courses.append(Course(course_name, course_id))
            self.marks[course_id] = []

    def inputMarks(self):
        cid = input("Course ID: ")
        if cid not in self.marks:
            print("Not found")
            return

        print(f"Now you are entering marks for course {cid} my bigga")
        for student in self.students:
            m = float(input(f"Marks for {student.getName()}: "))
            self.marks[cid].append(Mark(student, m))

    def printStudents(self):
        print("\nStudents:")
        for student in self.students:
            student.info()

    def printCourses(self):
        print("\nCourses:")
        for course in self.courses:
            course.info()

    def printMarks(self):
        cid = input("Course ID: ")
        if cid not in self.marks:
            print("Not found")
            return

        for mark in self.marks[cid]:
            print(f"{mark.getStudent().getName()}: {mark.getMark()}")

    def main(self):
        while True:
            print("\n--- Student Mark Management System ---")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.inputStudents()
            elif choice == "2":
                self.inputCourses()
            elif choice == "3":
                self.inputMarks()
            elif choice == "4":
                self.printStudents()
            elif choice == "5":
                self.printCourses()
            elif choice == "6":
                self.printMarks()
            elif choice == "0":
                print("Exiting, goodbye my fella !!!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    usa = USA_shooting_area()
    usa.main()
