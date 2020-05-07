class Square():
    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.s1, self.s1, self.s1, self.s1)

sqr = Square(4)
print(sqr.__repr__())

class Name():
    def __init__(self):
        self.name = 'bob'

name1 = Name()
name2 = Name()
name3 = name1

def mainFunction(name1, name2, name3):
    print('name1 is name2 ', name1 is name2)
    print('name1 is name3 ', name1 is name3)

mainFunction(name1, name2, name3)