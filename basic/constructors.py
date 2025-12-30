# class Point:
#     def __init__(self,x,y): # constructors are special methods invoked when a class object is made
#         self.x = x
#         self.y = y

# point = Point(10,20)
# print(point.x)

# task

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello {name}")
    def talk(self):
        print(f"Hi i am {self.name}")

mohit = Person("Mohit")
mohit.talk()

manglani = Person("Manglani")
manglani.talk()