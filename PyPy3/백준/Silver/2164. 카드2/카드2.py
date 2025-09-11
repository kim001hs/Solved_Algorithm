from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
queue=deque([(n-i) for i in range(n)])
index=0
arr=[(n-_) for _ in range(n)]
for i in range(n-1):
    queue.pop()
    queue.insert(0, queue.pop())
print(queue.pop())