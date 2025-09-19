import sys
from collections import deque
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
n=int(input())
is_black=list(input())#0이 하얀색
visited=[False]*n
graph=[[]for i in range(n)]
count=0
for i in range(n-1):
    t1,t2=map(int, input().split())
    graph[t1-1].append(t2-1)
    graph[t2-1].append(t1-1)

for i in range(n):
    temp=0
    queue=deque()
    if is_black[i]=='1':
        for j in graph[i]:
            if is_black[j]=='1':
                count+=1
    else:
        if visited[i]:
            continue
        for j in graph[i]:
            if is_black[j]=='1':
                temp+=1
            else:
                if not visited[j]:
                    queue.append(j)
    visited[i]=True
    while queue:
        L=queue.popleft()
        visited[L]=True
        if is_black[L]=='1':
            for j in graph[L]:
                if is_black[j]=='1':
                    count+=1
        else:
            for j in graph[L]:
                if is_black[j]=='1':
                    temp+=1
                else:
                    if not visited[j]:
                        queue.append(j)
    count+=temp*(temp-1)

print(count)