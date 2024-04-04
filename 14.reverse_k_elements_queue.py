
from sys import stdin
import queue


def reverse(q):
    if q.qsize() <= 1:
        return
    front = q.get()
    reverse(q)
    q.put(front)

def reverseKElements(inputQueue, k):

    temp = queue.Queue()
    while k > 0:
        temp.put(inputQueue.get())
        k = k - 1
    reverse(temp)
    
    while not inputQueue.empty():
        temp.put(inputQueue.get())
    return temp

def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
