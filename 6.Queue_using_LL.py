
from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def getSize(self):
        return self.__count

    def isEmpty(self) :
        return self.getSize() == 0

    def enqueue(self, data) :
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode

        self.__tail = newNode
        self.__count = self.__count + 1

    def dequeue(self) :
        if self.__head is None:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return data

    def front(self) :
        if self.__head is None:
            return -1
        data = self.__head.data
        return data


q = int(stdin.readline().strip())

queue = Queue()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2 :
        print(queue.dequeue())

    elif choice == 3 :
        print(queue.front())

    elif choice == 4 : 
        print(queue.getSize())

    else :
        if queue.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
