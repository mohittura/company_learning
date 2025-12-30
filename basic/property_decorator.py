class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter #setter method to add some rules
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter #setter method to add some rules
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectangle(4,5) # lower than zero values will work here as the private variables are accessed directly

rectangle.height = -5

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)