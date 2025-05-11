from person import Person

class Student(Person):
    def __init__(self, name: str, email: str, student_id: str, major: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.major = major

    def get_role(self) -> str:
        return "Student"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["email"], data["student_id"], data["major"])
