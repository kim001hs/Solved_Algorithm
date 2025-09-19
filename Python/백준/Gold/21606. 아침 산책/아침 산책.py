import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
m=int(input()[::-1],2)
graph=[[]for i in range(n)]
count=0
for i in range(n-1):
    t1,t2=map(int, input().split())
    graph[t1-1].append(t2-1)
    graph[t2-1].append(t1-1)
    
def dfs(visited, cur):
    global count
    visited |= (1<<cur)
    for i in graph[cur]:
        if not (visited & (1<<i)):
            if (1<<i) & m:
                count+=1
                continue
            dfs(visited,i)
    return

for i in range(n):
    visited=0
    if (1<<i) & m:
        dfs(visited,i)
print(count)