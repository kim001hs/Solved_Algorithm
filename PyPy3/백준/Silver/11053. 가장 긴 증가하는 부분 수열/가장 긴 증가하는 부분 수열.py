import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(int,input().split()))
dp=[1 for _ in range(N)]
max_=0
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
    max_=max(max_,dp[i])
print(max_)