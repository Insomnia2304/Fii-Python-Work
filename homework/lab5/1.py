class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, value):
        self.__stack += [value]

    def pop(self):
        if self.is_empty():
            return None
        peek = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return peek
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__stack[-1]

    def __str__(self):
        return self.__stack.__str__()

s = Stack()
print(s.peek())

for i in range(10):
    s.push(i)
print(s)

print(s.pop())
print(s.pop())
print(s)
print(s.peek())
