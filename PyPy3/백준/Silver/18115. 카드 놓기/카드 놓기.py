import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int, input().split()))
res=deque()
for i in range(N-1,-1,-1):
    j=N-i
    if arr[i]==1:
        res.appendleft(j)
    elif arr[i]==2:
        temp=res.popleft()
        res.appendleft(j)
        res.appendleft(temp)
    elif arr[i]==3:
        res.append(j)
print(*res)