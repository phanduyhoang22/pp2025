import curses
from curses import wrapper
import input as ip
import output as op

def main(stdscr):
    # Khoi tao danh sach
    students = []
    courses = []

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "================ PW4 MODULAR MENU ================")
        stdscr.addstr(1, 0, "1. Nhap sinh vien")
        stdscr.addstr(2, 0, "2. Nhap mon hoc")
        stdscr.addstr(3, 0, "3. Nhap diem")
        stdscr.addstr(4, 0, "4. Hien thi danh sach")
        stdscr.addstr(5, 0, "5. Thoat")
        stdscr.addstr(7, 0, "Chon chuc nang: ")
        
        try:
            choice = int(stdscr.getkey()) - 48
        except:
            choice = 0

        if choice == 1:
            ip.input_students(stdscr, students)
        elif choice == 2:
            ip.input_courses(stdscr, courses)
        elif choice == 3:
            ip.input_marks(stdscr, students, courses)
        elif choice == 4:
            op.show_list(stdscr, students, courses)
        elif choice == 5:
            break

if __name__ == "__main__":
    wrapper(main)