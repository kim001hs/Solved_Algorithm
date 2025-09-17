import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
V, E=map(int,input().split())
K=int(input())-1
INF=int(1e9)
graph=[[] for _ in range(V)]
dist=[INF for _ in range(V)]
for i in range(E):
    t1,t2,t3=map(int, input().split())
    graph[t1-1].append([t3,t2-1])
def dijkstra():
    dist=[INF for _ in range(V)]
    dist[K]=0
    pq=[]
    heapq.heappush(pq,[0,K])
    while pq:
        weight,spot=heapq.heappop(pq)
        if weight>dist[spot]:
            continue
        
        for w,s in graph[spot]:
            next_w=w+weight
            if next_w<dist[s]:
                dist[s]=next_w
                heapq.heappush(pq,[next_w,s])
    
    return dist
result=dijkstra()                
for i in range(V):
    print(result[i] if result[i]!=INF else "INF")