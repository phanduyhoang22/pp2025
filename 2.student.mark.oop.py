class Student:
    def __init__(self, sid, name, dob):
        self._sid = sid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._sid
    
    def get_name(self):
        return self._name
    
    def get_dob(self):
        return self._dob
    
    def display(self):
        print(f"ID: {self._sid} | Tên: {self._name} | Ngày: {self._dob}")

class Course:
    def __init__(self, cid, name):
        self._cid = cid
        self._name = name

    def get_id(self):
        return self._cid
    
    def get_name(self):
        return self._name
    
    def display(self):
        print(f"ID: {self._cid} | Tên môn học: {self._name}")

class System:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        try:
            num = int(input("Nhập số lượng sinh viên: "))
            for _ in range(num):
                print("--- Nhập thông tin sinh viên ---")
                sid = input("ID: ")
                name = input("Tên: ")
                dob = input("DD/MM/YYYY: ")
                self.students.append(Student(sid, name, dob))
        except ValueError:
            print("Error!")

    def input_courses(self):
        try:
            num = int(input("Nhập số lượng môn học: "))
            for _ in range(num):
                print("--- Nhập thông tin môn học ---")
                cid = input("ID: ")
                name = input("Tên môn học: ")
                self.courses.append(Course(cid, name))
        except ValueError:
            print("Error!")

    def list_students(self):
        print("\n--- Danh sách sinh viên ---")
        for s in self.students:
            s.display()

    def list_courses(self):
        print("\n--- Danh sách môn học ---")
        for c in self.courses:
            c.display()

    def input_marks(self):
        print("--- Nhập điểm ---")
        self.list_courses()
        cid = input("Nhập ID môn học để nhập điểm: ")

        course_exists = False
        for c in self.courses:
            if c.get_id() == cid:
                course_exists = True
                break

        if not course_exists:
            print("ID môn học không tồn tại!")
            return
    
        for s in self.students:
            try:
                mark = float(input(f"Nhập điểm: {s.get_name()} | ID: {s.get_id()}: "))
                data = {'course_id': cid, 'student_id': s.get_id(), 'mark': mark}
                self.marks.append(data)
            except ValueError:
                print("Error!")

    def show_marks(self):
        print("\n--- Xem bảng điểm ---")
        self.list_courses()
        cid = input("Nhập ID môn học cần xem: ")

        print(f"\nBảng điểm môn {cid}: ")
        found = False
        for m in self.marks:
            if m['course_id'] == cid:
                s_name = "Unknown"
                for s in self.students:
                    if s.get_id() == m['student_id']:
                        s_name = s.get_name()
                        break
                print(f"Sinh viên: {s_name} - Điểm: {m['mark']}")
                found = True

        if not found:
            print("Không thấy!")

if __name__ == "__main__":
    system = System()

    while True:
        print("\n--- Menu ---")
        print("1. Sinh viên")
        print("2. Môn học")
        print("3. Danh sách sinh viên")
        print("4. Danh sách môn học")
        print("5. Nhập điểm")
        print("6. Xem điểm")
        print("7. Thoát")      

        choice = input("Chọn 1 - 7: ")

        if choice == '1':
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.list_students()
        elif choice == '4':
            system.list_courses()
        elif choice == '5':
            system.input_marks()
        elif choice == '6':
            system.show_marks()
        elif choice == '7':
            print("Thoát!")
            break
        else:
            print("Chọn lại!")