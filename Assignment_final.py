# Define a class for courses
class Course:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

# Define a class for students
class Student:
	def __init__(self, name):
		self.name = name
		self.courses = []

	def add_course(self, course):
		self.courses.append(course)

	def get_courses(self):
		return self.courses

# Create some courses
math101 = Course("Math 101", 3)
cs102 = Course("Computer Science 102", 4)
english101 = Course("English 101", 3)

# Create a student
student1 = Student("Asadullah")

# Add courses to the student
student1.add_course(math101)
student1.add_course(cs102)
student1.add_course(english101)

# Print the student's courses
print(student1.name, "is taking:")
for course in student1.get_courses():
	print(course.name, "(", course.credits, "credits)")



