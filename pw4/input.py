import curses
import math
from domains import Student, Course, Mark

def get_input(stdscr, prompt):
    stdscr.addstr(prompt)
    curses.echo()
    input_str = stdscr.getstr().decode('utf-8')
    curses.noecho()
    return input_str

def input_students(stdscr):
    stdscr.clear()
    students = []
    try:
        n = int(get_input(stdscr, "Number of students: "))
        for i in range(n):
            stdscr.addstr(f"\n--- Student {i + 1} ---\n")
            name = get_input(stdscr, "Name: ")
            sid = get_input(stdscr, "ID: ")
            dob = get_input(stdscr, "DOB: ")
            students.append(Student(name, sid, dob))
    except ValueError:
        stdscr.addstr("\nInvalid input. Press any key.")
        stdscr.getch()
    return students

def input_courses(stdscr):
    stdscr.clear()
    courses = []
    try:
        n = int(get_input(stdscr, "Number of courses: "))
        for i in range(n):
            stdscr.addstr(f"\n--- Course {i + 1} ---\n")
            name = get_input(stdscr, "Course Name: ")
            cid = get_input(stdscr, "Course ID: ")
            credit = get_input(stdscr, "Credits: ")
            courses.append(Course(name, cid, credit))
    except ValueError:
        stdscr.addstr("\nInvalid input. Press any key.")
        stdscr.getch()
    return courses

def input_marks(stdscr, students, courses):
    stdscr.clear()
    cid = get_input(stdscr, "Enter Course ID to input marks: ")
    # Logic to verify course exists and collect marks
    marks_list = []
    for student in students:
        m = float(get_input(stdscr, f"Mark for {student.getName()}: "))
        m = math.floor(m * 10) / 10
        marks_list.append(Mark(student, m))
    return cid, marks_list