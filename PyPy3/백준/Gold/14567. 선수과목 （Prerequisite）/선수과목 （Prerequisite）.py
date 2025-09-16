from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
gnum=[0]*N
for i in range(M):
    t1,t2=map(int,input().split())
    graph[t1-1].append(t2-1)
    gnum[t2-1]+=1
    
def topology_sort():
    result=[1]*N
    queue=deque()
    for i in range(N):
        if gnum[i]==0:
            queue.append(i)
    while queue:
        temp=queue.popleft()
        for i in graph[temp]:
            gnum[i]-=1
            if gnum[i]==0:
                queue.append(i)
                result[i]=result[temp]+1
    return result
print(*topology_sort())