import curses

def draw_menu(stdscr, title, options):
    stdscr.clear()
    stdscr.addstr(1, 2, f"=== {title} ===", curses.A_BOLD)
    for idx, option in enumerate(options):
        stdscr.addstr(3 + idx, 4, f"{idx + 1}. {option}")
    stdscr.addstr(3 + len(options), 4, "0. Back/Exit")
    stdscr.refresh()

def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(1, 2, "STUDENT LIST", curses.A_UNDERLINE)
    for i, s in enumerate(students):
        stdscr.addstr(3 + i, 2, str(s))
    stdscr.addstr("\n\nPress any key to return.")
    stdscr.getch()

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(1, 2, "COURSE LIST", curses.A_UNDERLINE)
    for i, c in enumerate(courses):
        stdscr.addstr(3 + i, 2, f"ID: {c.getCourseId():<10} | Name: {c.getCourseName():<15} | Credits: {c.getCredits()}")
    stdscr.addstr("\n\nPress any key to return.")
    stdscr.getch()