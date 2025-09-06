import sys
input = sys.stdin.readline
INF=int(1e9)
n= int(input())
graph=[]
dp=[[INF]*(1<<n) for _ in range(n)]
for i in range(n):
    data=list(map(int, input().split()))
    processed_data = [INF if d == 0 else d for d in data]
    graph.append(processed_data)
def dfs(start,visited):
    if visited == (1<<n)-1:
        dp[start][visited]=graph[start][0]
        return graph[start][0]
    if dp[start][visited]!=INF:
        return dp[start][visited]
    for i in range(n):
        if visited & (1<<i):
            continue
        dp[start][visited]=min(dp[start][visited], dfs(i, visited | (1<<i))+graph[start][i])
    return dp[start][visited]

print(dfs(0,1))