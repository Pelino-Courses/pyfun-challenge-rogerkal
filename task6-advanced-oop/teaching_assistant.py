from student import Student
from instructor import Instructor
from person import Person  

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str, email: str, student_id: str, major: str, employee_id: str, department: str):
        Person.__init__(self, name, email)
        self.student_id = student_id
        self.major = major
        self.employee_id = employee_id
        self.department = department
        self.courses = []

    def get_role(self) -> str:
        return "Teaching Assistant"
