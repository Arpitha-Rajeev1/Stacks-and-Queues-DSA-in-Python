import queue

#inbuilt stack as list
s = [1,2,3]
s.append(4)
print(s.pop())
print(s.pop())

#inbuilt queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

while not q.empty():
    print(q.get())

#build stack using queue
s = queue.LifoQueue()
s.put(1)
s.put(2)
s.put(3)

while not s.empty():
    print(s.get())
    
