from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
        
    def list_students(self):
        for num, student in enumerate(self.students, start=1):
            print(f"{num}. {student}")
