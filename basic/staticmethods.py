class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    

    # This is an instance method as it works on the objects of the classes (instance)
    def get_info(self):
        return f"{self.name} works as {self.position}"
    
    @staticmethod # belongs to a class but not the objects
    def is_valid_pos(position): # We will not define "self" as an arguement as it will not work directly on the instances of the class
        valid_position = ["Manager", "Cleaner", "Cook", "Marketing Manager", "HR"]
        return position in valid_position
    
print(Employee.is_valid_pos("Cook")) # it is called by the class name rather than an object of that class