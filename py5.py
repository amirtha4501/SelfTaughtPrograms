class Shape():
    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length   
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return 4 * self.s1

    def change_size(self, new_size):
        self.s1 += new_size
        return self.s1

rect = Rectangle(2, 2)
rect.what_am_i()
print('The perimeter of a rectangle is ', rect.calculate_perimeter())

sqr = Square(4)
sqr.what_am_i()
print('The perimeter of a square is ', sqr.calculate_perimeter())
print('New size is ', sqr.change_size(3))
