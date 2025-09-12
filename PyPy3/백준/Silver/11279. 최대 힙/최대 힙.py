from heapq import heappush,heappop
import sys
input=sys.stdin.readline
arr=[]
n=int(input())
for i in range(n):
    m=int(input())
    if m==0:
        if len(arr)==0:
            print(0)
        else:
            print(-heappop(arr))
    else:
        heappush(arr,-m)