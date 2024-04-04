class Queue:
    def __int__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, data):
        self.__arr.append(data)

    def dequeue(self):
        if self.__count == 0:
            return -1
        element = self.__arr[self.__front]
        self.__front += 1
        return element

    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0


def __int__(self):
        self.__arr = list()

    def insertFront(self, ele):
        self.__arr.insert(0, ele)

    def insertRear(self, ele):
        self.__arr.append(ele)

    def deleteFront(self):
        if len(self.__arr) == 0:
            return -1
        ele = self.__arr[0]
        del self.__arr[0]
        return ele

    def deleteRear(self):
        if len(self.__arr) == 0:
            return -1
        ele = self.__arr[-1]
        del self.__arr[-1]
        return ele

    def getFront(self):
        if len(self.__arr) == 0:
            return -1
        ele = self.__arr[0]
        return ele

    def getRear(self):
        if len(self.__arr) == 0:
            return -1
        ele = self.__arr[-1]
        return ele
