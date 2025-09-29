import sys
import heapq
input = sys.stdin.readline
n=int(input())
arr1=list(map(int, input().split()))#
m=int(input())
arr2=list(map(int,input().split()))
result=[]
pq=[]
max,midx=0,0
for i in range(n):
    for j in range(m):
        if arr1[i]==arr2[j]:
            heapq.heappush(pq, (-arr1[i], i, j))
prev_i,prev_j=-1,-1
while pq:
    temp=heapq.heappop(pq)
    if temp[1]>prev_i and temp[2]>prev_j:
        prev_i,prev_j=temp[1],temp[2]
        result.append(-temp[0])
print(len(result))
print(*result)