import curses
import math
import numpy as np


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

    def setDoB(self, dob):
        self._dob = dob

    def __str__(self):
        return f"ID: {self._id:<10} | Name: {self._name:<15} | GPA: {self._gpa:.1f}"


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
        return int(self._credits)


class Mark:
    def __init__(self, student, mark):
        self._student = student
        self._mark = mark

    def getStudent(self): return self._student

    def getMark(self): return self._mark


class SchoolSystem:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = {}  # course_id: [Mark objects]

    def draw_menu(self, title, options):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        self.stdscr.addstr(1, 2, f"=== {title} ===", curses.A_BOLD)

        for idx, option in enumerate(options):
            self.stdscr.addstr(3 + idx, 4, f"{idx + 1}. {option}")

        self.stdscr.addstr(3 + len(options), 4, "0. Back/Exit")
        self.stdscr.refresh()

    def get_input(self, prompt):
        self.stdscr.addstr(prompt)
        curses.echo()
        input_str = self.stdscr.getstr().decode('utf-8')
        curses.noecho()
        return input_str

    def input_students(self):
        self.stdscr.clear()
        try:
            n = int(self.get_input("Number of students: "))
            for i in range(n):
                self.stdscr.addstr(f"\n--- Student {i + 1} ---\n")
                name = self.get_input("Name: ")
                sid = self.get_input("ID: ")
                dob = self.get_input("DOB: ")
                self.students.append(Student(name, sid, dob))
        except ValueError:
            self.stdscr.addstr("\nInvalid input. Press any key.")
            self.stdscr.getch()

    def input_courses(self):
        self.stdscr.clear()
        try:
            n = int(self.get_input("Number of courses: "))
            for i in range(n):
                self.stdscr.addstr(f"\n--- Course {i + 1} ---\n")
                name = self.get_input("Course Name: ")
                cid = self.get_input("Course ID: ")
                credit = self.get_input("Credits: ")
                self.courses.append(Course(name, cid, credit))
                self.marks[cid] = []
        except ValueError:
            self.stdscr.addstr("\nInvalid input. Press any key.")
            self.stdscr.getch()

    def input_marks(self):
        self.stdscr.clear()
        cid = self.get_input("Enter Course ID to input marks: ")
        if cid not in self.marks:
            self.stdscr.addstr("\nCourse not found! Press any key.")
            self.stdscr.getch()
            return

        for student in self.students:
            m = float(self.get_input(f"Mark for {student.getName()}: "))
            m = math.floor(m * 10) / 10
            self.marks[cid].append(Mark(student, m))

    def list_students(self):
        self.stdscr.clear()
        self.stdscr.addstr(1, 2, "STUDENT LIST", curses.A_UNDERLINE)
        for i, s in enumerate(self.students):
            self.stdscr.addstr(3 + i, 2, str(s))
        self.stdscr.addstr("\n\nPress any key to return.")
        self.stdscr.getch()

    def list_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr(1, 2, "COURSE LIST", curses.A_UNDERLINE)
        for i, c in enumerate(self.courses):
            self.stdscr.addstr(3 + i, 2,
                               f"ID: {c.getCourseId():<10} | Name: {c.getCourseName():<15} | Credits: {c.getCredits()}")
        self.stdscr.addstr("\n\nPress any key to return.")
        self.stdscr.getch()

    def calculate_gpas(self):
        for student in self.students:
            total_weighted = 0
            total_credits = 0
            for course in self.courses:
                cid = course.getCourseId()
                course_marks = self.marks.get(cid, [])
                for m in course_marks:
                    if m.getStudent().getId() == student.getId():
                        total_weighted += m.getMark() * course.getCredits()
                        total_credits += course.getCredits()

            if total_credits > 0:
                gpa = total_weighted / total_credits
                student.setGPA(math.floor(gpa * 10) / 10)
            else:
                student.setGPA(0.0)

    def sort_students(self):
        self.calculate_gpas()
        # Using a simple sort based on GPA
        self.students.sort(key=lambda x: x.getGPA(), reverse=True)
        self.stdscr.addstr("\nStudents sorted by GPA. Press any key to view.")
        self.stdscr.getch()
        self.list_students()

    def run(self):
        options = [
            "Input Students", "Input Courses", "Input Marks",
            "List Students", "List Courses", "Calculate GPAs", "Sort by GPA"
        ]

        while True:
            self.draw_menu("STUDENT MANAGEMENT SYSTEM", options)
            choice = self.get_input("\nChoose an option: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.calculate_gpas()
                self.stdscr.addstr("\nGPAs Calculated! Press any key.")
                self.stdscr.getch()
            elif choice == "7":
                self.sort_students()
            elif choice == "8":
                break
            else:
                self.stdscr.addstr("\nInvalid choice. Press any key.")
                self.stdscr.getch()


def main(stdscr):
    # Initial Curses Setup
    curses.curs_set(0)  # Hide cursor
    system = SchoolSystem(stdscr)
    system.run()


if __name__ == "__main__":
    curses.wrapper(main)