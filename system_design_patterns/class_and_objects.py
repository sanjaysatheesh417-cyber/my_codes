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

xyz = school()
print(id(xyz))
xyz.add_school_name("xyz school")
xyz.add_student("sara")
xyz.add_student("bala")
xyz.add_student("sara_2")
xyz.add_student("bala_3")

abc.get_number_of_student()
xyz.get_number_of_student()

#user defined constructor
class school:
    def __init__(self,name):#sonstructor
        print("constructor is invoked")
        print(f"school create with name {name}")
        self.name = name
        self.list_student = []
    def add_student(self,student_name):
        self.list_student.append(student_name)
    def remove_student(self,student_name):
        self.list_student.remove(student_name)
    def get_number_of_student(self):
        print(f"The number of student in a school {self.name} is {len(self.list_student)}")
    def get_student_list(self):
        for student in self.list_student:
            print(student)

abc = school("abc school")
abc.add_student("priyal")
abc.add_student("balakrishna")
abc.add_student("mahender")
abc.get_student_list()

xyz = school("xyz school")
xyz.add_student("sara")
xyz.add_student("bala")
xyz.add_student("sara_2")
xyz.add_student("bala_3")

#user defined destructor
del xyz

class school:
    def __init__(self,name):#sonstructor
        print("constructor is invoked")
        print(f"school create with name {name}")
        self.name = name
        self.list_student = []
    def add_student(self,student_name):
        self.list_student.append(student_name)
    def remove_student(self,student_name):
        self.list_student.remove(student_name)
    def get_number_of_student(self):
        print(f"The number of student in a school {self.name} is {len(self.list_student)}")
    def get_student_list(self):
        for student in self.list_student:
            print(student)
    def __del__(self):
        print(f"all {len((self.list_student))} students are transferred to new schools")

xyz = school("xyz school")
xyz.add_student("sara")
xyz.add_student("bala")
xyz.add_student("sara_2")
xyz.add_student("bala_3")

del xyz

#oops inheritance
class school:
    def __init__(self,name):#sonstructor
        print("constructor is invoked")
        print(f"school create with name {name}")
        self.name = name
        self.list_student = []
    def add_student(self,student_name):
        self.list_student.append(student_name)
    def remove_student(self,student_name):
        self.list_student.remove(student_name)
    def get_number_of_student(self):
        print(f"The number of student in a school {self.name} is {len(self.list_student)}")
    def get_student_list(self):
        for student in self.list_student:
            print(student)
    def __del__(self):
        print(f"all {len((self.list_student))} students are transferred to new schools")

class CBSE(school):
    def __init__(self,name):
        #school.__init__(self,name)
        super().__init__(name)
    def teaching_method(self):
        print(f"CBSE Syllabus")

bit_CBSE = CBSE("bits school")

bit_CBSE.add_student("sara")
bit_CBSE.add_student("vinay")
bit_CBSE.add_student("priyal")

bit_CBSE.get_number_of_student()
bit_CBSE.get_student_list()
del bit_CBSE

class A:
    def __init__(self,name):
        self.name = name