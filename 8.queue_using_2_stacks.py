from os import *
from sys import *
from collections import *
from math import *


class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, data):
        while(len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())

        self.__s1.append(data)

        while(len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())

        return True

    def dequeue(self):
        if(len(self.__s1) == 0):
            return -1
        return self.__s1.pop()
