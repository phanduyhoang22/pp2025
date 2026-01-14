import curses

def show_list(stdscr, students, courses):
    stdscr.clear()
    
    for s in students:
        s.calculate_gpa(courses)
    
    students.sort(key=lambda x: x._gpa, reverse=True)

    stdscr.addstr(0, 0, "--- DANH SACH SINH VIEN (Sap xep theo GPA) ---")
    for idx, s in enumerate(students):
        stdscr.addstr(2 + idx, 0, str(s))
    
    stdscr.getch()