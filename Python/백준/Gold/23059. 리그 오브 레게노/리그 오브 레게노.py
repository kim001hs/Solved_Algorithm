from collections import deque
import sys
from collections import defaultdict
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
graph=defaultdict(list)
count=defaultdict(int)
for i in range(n):
    start,end=map(str, input().split())
    graph[start].append(end)
    count[end]+=1
queue=deque()
for i in graph:
    if count[i]==0:
        queue.append((i,0))
result=[]
while queue:
    temp,num=queue.popleft()
    heapq.heappush(result,(num,temp))
    if temp in graph:
        for i in graph[temp]:
            count[i]-=1
            if count[i]==0:
                queue.append((i, num+1))
                
                
if len(count)==len(result):
    while result:
        temp=heapq.heappop(result)
        print(temp[1])
else:
    print(-1)