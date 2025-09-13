from heapq import heapify,heappop,heappush
import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
pq=[]
count=0
for i in range(n):
    heappush(pq, int(input()))
for i in range(n-1):
    temp=heappop(pq)
    temp+=heappop(pq)
    count+=temp
    heappush(pq,temp)
print(count)