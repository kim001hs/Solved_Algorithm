import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
for i in range(n):
    data=list(map(int,input().split()))
    arr.append(data)

def bfs(x,y):
    dp=[[0]*n for _ in range(n)]#방문할 수 있는 방법 수
    dp[x][y]=1
    for i in range(n):
        for j in range(n):
            if arr[i][j]>0:
                if i+arr[i][j]<n:
                    dp[i+arr[i][j]][j]+=dp[i][j]
                if j+arr[i][j]<n:
                    dp[i][j+arr[i][j]]+=dp[i][j]
    return dp[n-1][n-1]
print(bfs(0,0))