import sys
from collections import deque
import heapq
def input(): return sys.stdin.readline().rstrip()
T=int(input())
for _ in range(T):
    N,M=map(int, input().split())
    arr=deque(map(int, input().split()))
    ind=deque([i for i in range(N)])
    arr2=[]
    count=0
    for i in arr:
        heapq.heappush(arr2, -i)
    while arr:
        temp=arr.popleft()
        t_ind=ind.popleft()
        if temp==-arr2[0]:
            heapq.heappop(arr2)
            count+=1
            if t_ind==M:
                break
        else:
            arr.append(temp)
            ind.append(t_ind)
    print(count)