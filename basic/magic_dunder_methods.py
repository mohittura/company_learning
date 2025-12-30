class Employee:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"name: {self.name} and gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
em1 = Employee("patrick", 1.2)
em2 = Employee("plankton", 3.2)

print(em1 > em2)