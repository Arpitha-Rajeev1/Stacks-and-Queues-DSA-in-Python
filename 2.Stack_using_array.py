class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0

s = Stack()
s.push(2)
s.push(3)
print(s.top())
print(s)
