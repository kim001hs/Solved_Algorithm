from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
queue=deque([i for i in range(1,n+1)])
arr=[]
print('<',end='')
for i in range(n-1):
    for j in range(m-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end=", ")
print(queue.pop(),end='>')