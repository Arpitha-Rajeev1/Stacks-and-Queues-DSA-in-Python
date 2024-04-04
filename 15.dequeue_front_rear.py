from sys import stdin


class Dequeue:
    def __init__(self):
        self.arr = []
        self.size = 0

    # Inserts an element at front
    def insertFront(self, data):
        if self.size == 10:
            return -1
        self.arr.insert(0, data)
        self.size += 1

    def insertRear(self, data):
        if self.size == 10:
            return -1
        self.arr.append(data)
        self.size += 1

    def deleteFront(self):
        if (self.size == 0):
            return -1
        self.arr.pop(0)
        self.size -= 1

    def deleteRear(self):
        if (self.size == 0):
            return -1
        self.size -= 1

    def getFront(self):
        if (self.size == 0):
            return -1
        ele = self.arr[0]
        return ele

    def getRear(self):
        if (self.size == 0):
            return -1
        ele = self.arr[-1]
        return ele


queue = Dequeue()
inputs = stdin.readline().strip().split(" ")
c = len(inputs) - 1
i = 0

while i < c:

    choice = inputs[i]

    if choice == '1':
        data = inputs[i + 1]
        queue.insertFront(data)
        i += 2

    elif choice == '2':
        data = inputs[i + 1]
        queue.insertRear(data)
        i += 2

    elif choice == '3':
        ele = queue.deleteFront()
        if ele == -1:
            print(-1)
        i += 1

    elif choice == '4':
        ele = queue.deleteRear()
        if ele == -1:
            print(-1)
        i += 1

    elif choice == '5':
        print(queue.getFront())
        i += 1

    elif choice == '6':
        print(queue.getRear())
        i += 1

    else:
        i += 1
