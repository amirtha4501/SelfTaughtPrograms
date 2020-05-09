class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

stack = Stack()

word = "yesterday"

for c in word:
    stack.push(c)


reversed_string = ""


for i in range(len(stack.items)):
    reversed_string += stack.pop()


print(reversed_string)