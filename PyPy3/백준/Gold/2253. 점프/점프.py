import sys
from math import sqrt
def input(): return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
h=int(sqrt(2*n))
dp=[[-1]*(n+1) for i in range(h+1)]
dp[0][0]=0
dp[1][1]=0
blocked=[]
for _ in range(m):
    blocked.append(int(input()))
for j in range(2,n+1):
    for i in range(1,h+1):
        if j in blocked:
            continue
        if j<i:
            break
        if i<h:
            if dp[i+1][j-i]!=-1:
                dp[i][j]=dp[i+1][j-i]+1
        if dp[i-1][j-i]>0 or dp[i][j-i]>=0:
            for k in range(i,-1,-1):
                if dp[k][j-i]>=0:
                    if dp[i][j]==-1:
                        dp[i][j]=dp[k][j-i]+1
                        break
                    dp[i][j]=min(dp[k][j-i]+1,dp[i][j])
                    break
            if dp[i][j]==-1:
                dp[i][j]=dp[-1][j]

for i in range(h,0,-1):
    if dp[i][n]!=-1:
        print(dp[i][n])
        sys.exit()
print(-1)