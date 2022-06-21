import math

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year


name = input()
last = input()
year = input()

student = Student(name, last, year)
print(student.student_id)

math.fabs()
math.mean
math.sin()
math.cos()
math.sqrt()
