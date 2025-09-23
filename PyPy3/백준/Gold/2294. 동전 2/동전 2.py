import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,k=map(int,input().split())
arr=set()
INF=int(1e9)
dp=[0]+[INF]*(k)
count=0
for _ in range(n):
    arr.add(int(input()))
def solve():
    global dp
    for i in range(1,k+1):
        for j in arr:
            if i-j>=0 and dp[i-j]!=INF:
                dp[i]=min(dp[i-j]+1,dp[i])
    return dp[k] if dp[k]!=INF else -1
print(solve())