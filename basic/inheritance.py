class Animal:
    def walk (self):
        print("walk")

class Dog(Animal):
    def bark(self):
        print("bark")

class Cat(Animal):
    def meow(self):
        print("meow")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.meow()
cat1.walk()