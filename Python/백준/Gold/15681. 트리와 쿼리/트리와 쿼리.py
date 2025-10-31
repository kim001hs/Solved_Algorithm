import sys
sys.setrecursionlimit(200000)
def input(): return sys.stdin.readline().rstrip()
n,r,q=map(int,input().split())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    t1,t2=map(int,input().split())
    tree[t1].append(t2)
    tree[t2].append(t1)
dp=[1]*(n+1)
def dfs(node, parent):
    for child in tree[node]:
        if child!=parent:
            dfs(child, node)
            dp[node]+=dp[child]
dfs(r,0)
for _ in range(q):
    temp=int(input())
    print(dp[temp])