import sys
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().rstrip()
n,m=map(int, input().split())
visited=[0]*n
graph=[[]for i in range(n)]

for i in range(m):
    t1,t2=map(int,input().split())
    graph[t1-1].append(t2-1)
    graph[t2-1].append(t1-1)
stack=[]
count=0
for i in range(n):
    if not visited[i]:
        stack.append(i)
        while stack:
            temp=stack.pop()
            if temp==2:
                dsaf=11
            if visited[temp]==1:
                continue
            visited[temp]=1
            for i in graph[temp]:
                if visited[i]==0:
                    stack.append(i)
        count+=1
print(count)