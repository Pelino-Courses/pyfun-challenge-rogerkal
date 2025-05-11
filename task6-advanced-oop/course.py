class Course:
    def __init__(self, code: str, title: str, instructor):
        self.code = code
        self.title = title
        self.instructor = instructor
        self.students = []

    def __add__(self, student):
        self.students.append(student)
        return self

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return f"{self.code}: {self.title}"

