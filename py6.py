class Square():
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)
        
    def printer(self):
        print('The current objects are ', self.square_list)

sqr1 = Square(1)
sqr2 = Square(2)
sqr3 = Square(3)
sqr4 = Square(4)
sqr5 = Square(5)

sqr5.printer()

class Rect():
    rect_list = []

    def __init__(self):
        self.rect_list.append(self)
        print(self.rect_list)

rect1 = Rect()