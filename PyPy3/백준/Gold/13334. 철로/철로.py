import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
arr2=[]
for i in range(n):
    t1,t2=map(int,input().split())
    if t2<t1:
        t1,t2=t2,t1
    arr2.append([t1,t2])
    
d=int(input())
for i in arr2:
    if i[1]-i[0]<=d:
        arr.append(i)
arr.sort(key=lambda x:(x[1]))
max_count=0
heap=[]
for i in arr:
    while heap and heap[0][0]<i[1]-d:
        heapq.heappop(heap)
    
    heapq.heappush(heap, i)
    max_count=max(max_count,len(heap))
print(max_count)