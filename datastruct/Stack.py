# _*_ encoding:utf-8 _*_

class Stack:
    def __init__(self): self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    """
   查看栈顶但不移除
   """

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.is_empty())

s.push("dog")
s.push(4)
print(s.peek())

print(s.pop())
print(s.size())