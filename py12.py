class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



a_list = [1, 2, 3, 4, 5]

reversed_list = []

stack = Stack()

for item in a_list:
    stack.push(item)

for i in range(len(stack.items)):
    reversed_list.append(stack.pop())

print(reversed_list)