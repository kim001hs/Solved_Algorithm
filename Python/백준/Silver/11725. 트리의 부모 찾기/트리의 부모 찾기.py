import sys
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().rstrip()
n=int(input())
parent=[-1]*n
graph=[[] for _ in range(n)]
visited=[False]*n
for i in range(n-1):
    t1,t2=map(int, input().split())
    graph[t1-1].append(t2-1)
    graph[t2-1].append(t1-1)
stack=[0]
while stack:
    temp=stack.pop()
    for i in graph[temp]:
        if not visited[i]:
            visited[i]=True
            stack.append(i)
            parent[i]=temp+1
print(*parent[1:])