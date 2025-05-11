from person import Person

class Instructor(Person):
    def __init__(self, name: str, email: str, employee_id: str, department: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_role(self) -> str:
        return "Instructor"
