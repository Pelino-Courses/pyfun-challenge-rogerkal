from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

# Create people
alice = Student("Alice", "alice@example.com", "S001", "CS")
bob = Instructor("Bob", "bob@example.com", "I101", "CS")
ta = TeachingAssistant("Eve", "eve@example.com", "S002", "CS", "I102", "CS")

# Create course and assign instructor
cs101 = Course("CS101", "Intro to CS", bob)
bob.assign_course(cs101)

# Enroll students
cs101 + alice
cs101 + ta

# Print enrolled students
print(f"Students in {cs101.title}:")
for student in cs101:
    print(f" - {student.name} ({student.get_role()})")
