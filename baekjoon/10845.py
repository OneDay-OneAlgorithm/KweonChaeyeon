import sys
import queue

input = sys.stdin.readline
queue = queue.Queue()

n = int(input())

for _ in range(n):
    t = input().split()
    
    if t[0] == "push":
        queue.put(t[1])
    elif t[0] == "pop":
        if queue.empty():
            print(-1)
        else:
            print(queue.get())
    elif t[0] == "size":
        print(queue.qsize())
    elif t[0] == "empty":
        if queue.empty():
            print(1)
        else:
            print(0)
    elif t[0] == "front":
        if queue.empty():
            print(-1)
        else:
            print(queue.queue[0])
    elif t[0] == "back":
        if queue.empty():
            print(-1)
        else:
            print(queue.queue[-1])
            
