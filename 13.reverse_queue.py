
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

#using stack
def reverseQueue(inputQueue) :
    s = list()
    while not inputQueue.empty():
        s.append(inputQueue.get())
    while s:
        inputQueue.put(s.pop())

#reversing queue without using any other data structure
def reverse(q):
    if q.qsize() <= 1:
        return
    front = q.get()
    reverse(q)
    q.put(front)

def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1
