import math
import numpy as np
import curses
from curses import wrapper

class Student:
    def __init__(self, sid, name, dob):
        self._sid = sid
        self._name = name
        self._dob = dob
        self._marks = {}
        self._gpa = 0.0

    def get_id(self):
        return self._sid
    
    def get_name(self):
        return self._name
    
    def get_dob(self):
        return self._dob
    
    def get_marks(self):
        return self._marks
    
    def add_mark(self, cid, mark):
        self._marks[cid] = mark
        
    
    def cal_gpa(self, courses):
        scores = []
        credits = []

        for cid, mark in self._marks.items():
            for course in courses:
                if course.get_id() == cid:
                    scores.append(mark)
                    credits.append(course.get_credits())
                    break
        
        scores_arr = np.array(scores)
        credits_arr = np.array(credits)

        if len(scores) == 0:
            self._gpa = 0.0
        else:
            self._gpa = np.sum(scores_arr * credits_arr) / np.sum(credits_arr)

        return self._gpa
    
    def __str__(self):
        return f"ID: {self._sid} | Tên: {self._name} | GPA: {self._gpa: .2f}"
    
class Course:
    def __init__(self, cid, name, credits):
        self._cid = cid
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._cid
        
    def get_name(self):
        return self._name
        
    def get_credits(self):
        return self._credits
    
    def __str__(self):
        return f"ID: {self._cid} | Tên môn học: {self._name} | Tín chỉ: {self._credits}"
        
class System:
    def __init__(self):
        self.students = []
        self.courses = []

    def get_input(self, stdscr, prompt, y, x):
        stdscr.addstr(y, x, prompt)
        curses.echo() 
        input_str = stdscr.getstr(y, x + len(prompt)).decode('utf-8')
        curses.noecho()
        return input_str
    
    def input_students(self, stdscr):
        stdscr.clear()
        try:
            num = int(self.get_input(stdscr, "So luong sinh vien: ", 0, 0))
            for i in range(num):
                stdscr.addstr(2 + i*4, 0, f"--- Sinh vien {i+1} ---")
                sid = self.get_input(stdscr, "ID: ", 3 + i*4, 0)
                name = self.get_input(stdscr, "Ten: ", 4 + i*4, 0)
                dob = self.get_input(stdscr, "Ngay sinh: ", 5 + i*4, 0)
                self.students.append(Student(sid, name, dob))
        except ValueError:
            stdscr.addstr(10, 0, "Loi: Nhap so nguyen!")
            stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        try:
            num = int(self.get_input(stdscr, "So luong mon hoc: ", 0, 0))
            for i in range(num):
                stdscr.addstr(2 + i*4, 0, f"--- Mon hoc {i+1} ---")
                cid = self.get_input(stdscr, "ID: ", 3 + i*4, 0)
                name = self.get_input(stdscr, "Ten mon: ", 4 + i*4, 0)
                cred = int(self.get_input(stdscr, "Tin chi: ", 5 + i*4, 0))
                self.courses.append(Course(cid, name, cred))
        except ValueError:
            stdscr.addstr(10, 0, "Loi nhap lieu!")
            stdscr.getch()

    def input_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "--- Danh sach mon hoc ---")
        for idx, c in enumerate(self.courses):
            stdscr.addstr(1 + idx, 0, str(c))
        
        cid = self.get_input(stdscr, "Nhap ID mon hoc de nhap diem: ", len(self.courses) + 2, 0)
        
        selected_course = None
        for c in self.courses:
            if c.get_id() == cid:
                selected_course = c
                break
        
        if not selected_course:
            stdscr.addstr(len(self.courses) + 4, 0, "Khong tim thay mon hoc!")
            stdscr.getch()
            return

        for idx, s in enumerate(self.students):
            try:
                raw_mark = float(self.get_input(stdscr, f"Diem cho {s.get_name()}: ", len(self.courses) + 4 + idx, 0))
                mark = math.floor(raw_mark * 10) / 10
                s.add_mark(cid, mark)
            except ValueError:
                pass
        
        stdscr.addstr(len(self.courses) + len(self.students) + 5, 0, "Da nhap diem xong!")
        stdscr.getch()

    def show_list(self, stdscr):
        stdscr.clear()
        for s in self.students:
            s.cal_gpa(self.courses)
        
        self.students.sort(key=lambda x: x._gpa, reverse=True)

        stdscr.addstr(0, 0, "--- DANH SACH SINH VIEN (Sap xep theo GPA) ---")
        for idx, s in enumerate(self.students):
            stdscr.addstr(2 + idx, 0, str(s))
        
        stdscr.getch()

def main(stdscr):
    system = System()
    
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "--- Chọn ---")
        stdscr.addstr(1, 0, "1. Sinh viên")
        stdscr.addstr(2, 0, "2. Môn học (co tin chi)")
        stdscr.addstr(3, 0, "3. Nhập điểm (Làm tròn xuống)")
        stdscr.addstr(4, 0, "4. List và GPA")
        stdscr.addstr(5, 0, "5. Thoát")
        stdscr.addstr(7, 0, "Chọn chức năng: ")
        
        try:
            key = stdscr.getkey()
            choice = int(key) if key.isdigit() else 0
        except:
            choice = 0

        if choice == 1:
            system.input_students(stdscr)
        elif choice == 2:
            system.input_courses(stdscr)
        elif choice == 3:
            system.input_marks(stdscr)
        elif choice == 4:
            system.show_list(stdscr)
        elif choice == 5:
            break

if __name__ == "__main__":
    wrapper(main)