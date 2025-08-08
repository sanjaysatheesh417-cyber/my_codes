class school:
    def add_school_name(self,name):
        self.name = name
        self.list_student = []
    def add_student(self,student_name):
        self.list_student.append(student_name)
    def remove_student(self,student_name):
        self.list_student.remove(student_name)
    def get_number_of_student(self):
        print(f"The number of student is {len(self.list_student)}")
abc = school()
print(id(abc))

abc.add_school_name("abc school")

#classing a method
abc.add_student("priyal")
abc.add_student("balakrishna")
abc.add_student("mahender")

abc.get_number_of_student()

abc.remove_student("mahender")

abc.get_number_of_student()