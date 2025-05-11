class EnrollmentError(Exception):
    pass

class Enrollment:
    def __init__(self, student, course):
        if not hasattr(course, 'students'):
            raise EnrollmentError("Invalid course object")

        if student in course.students:
            raise EnrollmentError("Student already enrolled")

        course.students.append(student)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
