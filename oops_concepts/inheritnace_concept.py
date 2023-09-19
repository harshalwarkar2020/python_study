"""Single Inheritance:- One class can extend another class."""


class Teacher:
    subject1 = "Mathematics"
    subject2 = "Physics"

    def teacher_info(self):
        print("I am a Teacher of 8th Standard")

    def subject_info(self):
        print("Teaching {0} and {1}".format(self.subject1, self.subject2))


# Here the Student class inherits the Teacher class.

class Student(Teacher):
    roll_no = 12

    def std_info(self):
        print("I like is {0} and  {1} and my roll no is {2}".format(self.subject1, self.subject2, self.roll_no))


obj = Student()

obj.teacher_info()
obj.subject_info()
obj.std_info()

print("-----------------------------------------------")
"""Multiple Inheritance:- In multiple inheritance one class can extend more than one class."""


class Principal:
    school_name = "New City High School"

    def school_info(self):
        print("School name is {}".format(self.school_name))


class Teacher:
    subject1 = "Mathematics"
    subject2 = "Physics"

    def teacher_info(self):
        print("I am a Teacher of 8th Standard")

    def subject_info(self):
        print("Teaching {0} and {1}".format(self.subject1, self.subject2))


class Student(Principal, Teacher):
    roll_no = 12

    def std_info(self):
        print("I like is {0} and  {1} and my roll no is {2}".format(self.subject1, self.subject2, self.roll_no))
        print("Our School name is:- {}".format(self.school_name))


obj = Student()
obj.std_info()
obj.teacher_info()
obj.subject_info()
obj.school_info()
print("-----------------------------------------------")
