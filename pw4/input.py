import math
import curses
from domains.student import Student
from domains.course import Course

def get_input(stdscr, prompt, y, x):
    stdscr.addstr(y, x, prompt)
    curses.echo()
    input_str = stdscr.getstr(y, x + len(prompt)).decode('utf-8')
    curses.noecho()
    return input_str

def input_students(stdscr, students):
    stdscr.clear()
    try:
        num = int(get_input(stdscr, "So luong sinh vien: ", 0, 0))
        for i in range(num):
            stdscr.addstr(2 + i*4, 0, f"--- Sinh vien {i+1} ---")
            sid = get_input(stdscr, "ID: ", 3 + i*4, 0)
            name = get_input(stdscr, "Ten: ", 4 + i*4, 0)
            dob = get_input(stdscr, "Ngay sinh: ", 5 + i*4, 0)
            students.append(Student(sid, name, dob))
    except ValueError:
        stdscr.addstr(10, 0, "Loi: Nhap so nguyen!")
        stdscr.getch()

def input_courses(stdscr, courses):
    stdscr.clear()
    try:
        num = int(get_input(stdscr, "So luong mon hoc: ", 0, 0))
        for i in range(num):
            stdscr.addstr(2 + i*4, 0, f"--- Mon hoc {i+1} ---")
            cid = get_input(stdscr, "ID: ", 3 + i*4, 0)
            name = get_input(stdscr, "Ten mon: ", 4 + i*4, 0)
            cred = int(get_input(stdscr, "Tin chi: ", 5 + i*4, 0))
            courses.append(Course(cid, name, cred))
    except ValueError:
        stdscr.addstr(10, 0, "Loi nhap lieu!")
        stdscr.getch()

def input_marks(stdscr, students, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- Danh sach mon hoc ---")
    for idx, c in enumerate(courses):
        stdscr.addstr(1 + idx, 0, str(c))
    
    cid = get_input(stdscr, "Nhap ID mon hoc de nhap diem: ", len(courses) + 2, 0)
    
    course_exists = False
    for c in courses:
        if c.get_id() == cid:
            course_exists = True
            break
            
    if not course_exists:
        stdscr.addstr(len(courses) + 4, 0, "Khong tim thay mon hoc!")
        stdscr.getch()
        return

    for idx, s in enumerate(students):
        try:
            raw_mark = float(get_input(stdscr, f"Diem cho {s.get_name()}: ", len(courses) + 4 + idx, 0))
            mark = math.floor(raw_mark * 10) / 10
            s.add_mark(cid, mark)
        except ValueError:
            pass
    stdscr.addstr(len(courses) + len(students) + 5, 0, "Da nhap diem xong!")
    stdscr.getch()