from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1

    def pop(self):
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data

    def top(self):
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        return data

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.getSize() == 0


q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
