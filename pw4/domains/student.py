import numpy as np

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
    
    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark
    
    def get_marks(self):
        return self._marks

    def calculate_gpa(self, courses):
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
        return f"ID: {self._sid} | Tên: {self._name} | GPA: {self._gpa:.2f}"