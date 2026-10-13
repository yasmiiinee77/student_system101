class student :
    def __init__(self, name, id, grade):
        self.name= name
        self.id= id
        self.grade= grade
    def show_student(self):
        print ("Student Name :", self.name, "|", "Student ID :", self.id, "|", "Student Grade:", self.grade,"|")
student1= student("yasmine", "2033", 99.0)
student1.show_student()