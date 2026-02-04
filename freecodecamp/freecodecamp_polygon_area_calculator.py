import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        self.set_side(new_side)

    def set_height(self, new_side):
        self.set_side(new_side)

rect = Rectangle(20, 10)
print(rect.get_area())        # 200
print(rect.get_perimeter())   # 60
print(rect.get_diagonal())    # 22.36...
print(rect)                   # Rectangle(width=20, height=10)
print(rect.get_picture())     # 10 rows of 20 stars

sq = Square(5)
print(sq.get_area())          # 25
sq.set_width(2)
print(sq.get_area())          # 4
print(sq)                     # Square(side=2)

rect_large = Rectangle(10, 10)
rect_small = Rectangle(3, 3)
print(rect_large.get_amount_inside(rect_small)) # 9 (3 wide x 3 high)