class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa

        Student.count += 1

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
student1 = Student("SpongeBob", 3.2)
student2 = Student("Patrick", 1.2)
student3 = Student("Squidward", 3.7)    
print(Student.get_count())
