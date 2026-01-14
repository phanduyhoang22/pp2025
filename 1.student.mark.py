students = []
courses = []
marks = []

def input_number_of_students():
    count = int(input("Nhập số lượng sinh viên: "))
    return count

def input_student_info():
    print("\n--- Nhập thông tin sinh viên ---")
    sid = input("Nhập ID sinh viên: ")
    name = input("Nhập tên sinh viên: ")
    dob = input("Nhập ngày sinh (DD/MM/YYYY): ")
    student = {'id': sid, 'name': name, 'dob': dob}
    students.append(student)

def input_number_of_courses():
    count = int(input("Nhập số lượng môn học: "))
    return count

def input_course_info():
    print("\n--- Nhập thông tin môn học ---")
    cid = input("Nhập ID môn học: ")
    name = input("Nhập tên môn học: ")
    course = {'id': cid, 'name': name}
    courses.append(course)

def input_marks():
    print("\n--- Nhập điểm cho môn học ---")
    list_courses()
    course_id = input("Nhập ID môn học muốn nhập điểm: ")
    
    for student in students:
        mark = float(input(f"Nhập điểm cho sinh viên {student['name']} (ID: {student['id']}): "))
        data = {
            'course_id': course_id,
            'student_id': student['id'],
            'mark': mark
        }
        marks.append(data)

def list_students():
    print("\n--- Danh sách sinh viên ---")
    for s in students:
        print(f"ID: {s['id']}, Tên: {s['name']}, Ngày sinh: {s['dob']}")

def list_courses():
    print("\n--- Danh sách môn học ---")
    for c in courses:
        print(f"ID: {c['id']}, Tên: {c['name']}")

def show_student_marks():
    print("\n--- Xem điểm môn học ---")
    list_courses()
    course_id = input("Nhập ID môn học cần xem điểm: ")
    
    print(f"\nBảng điểm môn {course_id}:")
    for m in marks:
        if m['course_id'] == course_id:
            student_name = "Unknown"
            for s in students:
                if s['id'] == m['student_id']:
                    student_name = s['name']
                    break
            print(f"Sinh viên: {student_name} - Điểm: {m['mark']}")

def main():
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_info()

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_info()

    while True:
        print("\n================ SYSTEM MENU ================")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Hiển thị danh sách môn học")
        print("3. Nhập điểm cho môn học")
        print("4. Xem bảng điểm môn học")
        print("5. Thoát")
        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            list_students()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_student_marks()
        elif choice == '5':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()