# Student Mark Management System using normal data structures

students = [] # store dicts
courses = [] # also
marks = {} # i need an ABG asap

# input functions
def input_number_of_students():
    n = int(input("Enter number of students: "))
    return n

def input_student(n):
    for _ in range(n):
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Dob (dd/mm/yyyy): ")
        students.append({"id": sid, "name": name, "dob": dob})


def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    return n

def input_course(n):
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id": cid, "name": name})
        marks[cid] = []


def input_marks():
    course_id = input("Enter course ID to input marks: ")
    if course_id not in marks:
        print("Course not found.")
        return

    print(f"Entering marks for course {course_id}...")
    for stu in students:
        m = float(input(f"Mark for {stu['name']} (ID {stu['id']}): "))
        marks[course_id].append((stu["id"], m))


# listing functions
def list_courses():
    print("\nCourses:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")


def list_students():
    print("\nStudents:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")


def show_marks():
    course_id = input("Enter course ID to show marks: ")
    if course_id not in marks:
        print("Course not found")
        return

    print(f"\nMarks for course {course_id}:")
    for sid, m in marks[course_id]:
        # lookup student name
        name = next(s['name'] for s in students if s['id'] == sid)
        print(f"{name} (ID {sid}): {m}")


# main
def main():
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
            n = input_number_of_students()
            input_student(n)
        elif choice == "2":
            n = input_number_of_courses()
            input_course(n)
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "0":
            print("Exiting, goodbye my fella !!!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
