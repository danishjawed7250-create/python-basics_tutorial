#create a class to signify a student
class Student:
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_name("sehnaaz")    
print(student1.name)

student2 = Student()
student2.set_name("Alok")
print(student2.name)