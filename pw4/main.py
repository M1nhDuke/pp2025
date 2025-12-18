import curses
import math
import input
import output
from domains import Student, Course, Mark

class SchoolManager:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = {}  # course_id: [Mark objects]

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

    def run(self):
        # The 8 options as defined in your original source code
        options = [
            "Input Students",
            "Input Courses",
            "Input Marks",
            "List Students",
            "List Courses",
            "Calculate GPAs",
            "Sort by GPA"
        ]

        while True:
            output.draw_menu(self.stdscr, "STUDENT MANAGEMENT SYSTEM", options)
            choice = input.get_input(self.stdscr, "\nChoose an option: ")

            if choice == "1":
                self.students = input.input_students(self.stdscr)
            elif choice == "2":
                self.courses = input.input_courses(self.stdscr)
            elif choice == "3":
                cid, marks_list = input.input_marks(self.stdscr, self.students, self.courses)
                self.marks[cid] = marks_list
            elif choice == "4":
                output.list_students(self.stdscr, self.students)
            elif choice == "5":
                output.list_courses(self.stdscr, self.courses)
            elif choice == "6":
                self.calculate_gpas()
                self.stdscr.addstr("\nGPAs Calculated! Press any key.")
                self.stdscr.getch()
            elif choice == "7":
                self.calculate_gpas()
                # Sort based on GPA in descending order
                self.students.sort(key=lambda x: x.getGPA(), reverse=True)
                self.stdscr.addstr("\nStudents sorted by GPA. Press any key to view.")
                self.stdscr.getch()
                output.list_students(self.stdscr, self.students)
            elif choice == "8" or choice == "0":
                break
            else:
                self.stdscr.addstr("\nInvalid choice. Press any key.")
                self.stdscr.getch()

def main(stdscr):
    # Setup as per original requirements
    curses.curs_set(0)
    manager = SchoolManager(stdscr)
    manager.run()

if __name__ == "__main__":
    curses.wrapper(main)