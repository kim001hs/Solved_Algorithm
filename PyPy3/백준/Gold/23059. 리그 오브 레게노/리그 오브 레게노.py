from collections import deque
import sys
from collections import defaultdict
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
result=[[] for i in range(n*2)]
while queue:
    temp,num=queue.popleft()
    result[num].append(temp)
    if temp in graph:
        for i in graph[temp]:
            count[i]-=1
            if count[i]==0:
                queue.append((i, num+1))
for row in result:
    # 각 행(리스트)을 제자리에서 정렬(in-place sort)
    row.sort() 
if len(count)==sum(len(row) for row in result):
    for row in result:
        if row:
            print(*row, sep='\n')
else:
    print(-1)