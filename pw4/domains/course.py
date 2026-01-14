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
        return f"ID: {self._cid} | Môn: {self._name} | Tín chỉ: {self._credits}"