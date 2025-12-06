# Student Mark Management System using OOP, some advance features and curses-based UI

import math
import numpy as np

class Student:
    def __init__(self, name, id, dob):
        self._name = name
        self._id = id
        self._dob = dob
        self._gpa = 0

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

    def info(self):
        print(f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}, GPA: {self._gpa}")


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
        self.students = np.array()
        self.courses = np.array()
        self.marks = {} # key - value: course id - list of marks

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
            credit = input("Credits: ")
            self.courses.append(Course(course_name, course_id, credit))
            self.marks[course_id] = np.array()

    def inputMarks(self):
        cid = input("Course ID: ")
        if cid not in self.marks:
            print("Not found")
            return

        print(f"Now you are entering marks for course {cid} my bigga")
        for student in self.students:
            m = float(input(f"Marks for {student.getName()}: "))
            m = math.floor(m * 10) / 10
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

    def calculateGPA(self, student):
        total_weighted = 0
        total_credits = 0

        for course in self.courses:
            cid = course.get_id()
            for m in self.marks.get(cid, []):
                if m.get_student().get_id() == student.get_id():
                    total_weighted += course.get_credits() * m.get_mark()
            total_credits += course.get_credits()

            if total_credits == 0:
                student.set_gpa(0)
            else:
                gpa = total_weighted / total_credits
                student.set_gpa(math.floor(gpa * 10) / 10)

    def calculateGPAs(self):
        for stu in self.students:
            self.calculateGPA(stu)

    def sortGPA(self):
        self.calculateGPAs()
        self.students = np.array(sorted(self.students, key=lambda s: s.get_gpa(), reverse=True))
        self.printStudents()

    def main(self):
        while True:
            print("\n--- Student Mark Management System ---")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("7. Calculate all GPA")
            print("8. Sort by GPA")
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
            elif choice == "7":
                self.calculateGPAs()
                print("Finished calculating GPA my fella !!!")
            elif choice == "8":
                self.sortGPA()
            elif choice == "0":
                print("Exiting, goodbye my fella !!!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    usa = USA_shooting_area()
    usa.main()
