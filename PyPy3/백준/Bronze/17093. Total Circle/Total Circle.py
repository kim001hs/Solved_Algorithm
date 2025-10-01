import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
P,Q=[],[]
for i in range(n):
    t1,t2=map(int,input().split())
    P.append((t1,t2))
for j in range(m):
    t1,t2=map(int,input().split())
    Q.append((t1,t2))
result=0
for i in P:
    for j in Q:
        x=i[0]-j[0]
        y=i[1]-j[1]
        result=max(result,x**2+y**2)
print(result)