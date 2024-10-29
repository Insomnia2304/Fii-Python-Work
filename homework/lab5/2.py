class Queue:
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def push(self, value):
        self.__queue += [value]

    def pop(self):
        if self.is_empty():
            return None
        first = self.__queue[0]
        self.__queue = self.__queue[1:]
        return first
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__queue[0]

    def __str__(self):
        return self.__queue.__str__()

q = Queue()
print(q.peek())

for i in range(10):
    q.push(i)
print(q)

print(q.pop())
print(q.pop())
print(q)
print(q.peek())
