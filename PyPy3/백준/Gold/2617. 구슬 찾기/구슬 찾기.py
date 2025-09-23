from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
n,m=map(int, input().split())
bigger=[[] for _ in range(n)]#index보다 큰 수를 저장
smaller=[[] for _ in range(n)]#작은 수를 저장
for i in range(m):
    big,small=map(int,input().split())
    bigger[small-1].append(big-1)
    smaller[big-1].append(small-1)
    mid=(n+1)/2

def bfs(i,graph):#큰거보다 큰거보다 큰거보다 큰거...를 큐에 넣고 카운트
    count=0
    visited[i]=True
    queue=deque()
    queue.append(i)
    while queue:
        temp=queue.popleft()
        for j in graph[temp]:
            if not visited[j]:
                count+=1
                visited[j]=True
                queue.append(j)
    return count

result=0
for i in range(n):
    visited=[False]*n
    if bfs(i,bigger)>=mid:
        result+=1
    if bfs(i,smaller)>=mid:
        result+=1

print(result)