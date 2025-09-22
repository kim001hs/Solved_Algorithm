import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,m,k,x=map(int,input().split())
graph=[[] for i in range(n)]
INF=int(1e9)
for i in range(m):
    a,b=map(int, input().split())
    graph[a-1].append(b-1)
def dijkstra():
    dist=[INF]*n
    dist[x-1]=0
    queue=deque()
    for i in graph[x-1]:
        queue.append((i,1))
    while queue:
        s,d=queue.popleft()
        dist[s]=min(dist[s],d)
        for i in graph[s]:
            if k>=dist[s]+1 and dist[s]+1<dist[i]:
                queue.append((i,dist[s]+1))
    return dist
result=dijkstra()
count=0
for index,i in enumerate(result):
    if i==k:
        print(index+1)
        count+=1
if count==0:
    print(-1)