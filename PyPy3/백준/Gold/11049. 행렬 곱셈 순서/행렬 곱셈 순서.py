import sys
input = sys.stdin.readline
n=int(input())
arr=[]
dp=[[-1]*n for _ in range(n)]
for i in range(n):
    data=list(map(int, input().split()))
    arr.append(data)

def dfs(start,end):
    if dp[start][end]!=-1:
        return dp[start][end]
    if start==end:
        dp[start][end]=0
        return 0
    if end-start==1:
        dp[start][end]=arr[start][0]*arr[start][1]*arr[end][1]
        return dp[start][end]
    
    for index in range (start,end):
        if  dp[start][end]==-1:
            dp[start][end]= dfs(start,index)+dfs(index+1,end)+arr[start][0]*arr[index][1]*arr[end][1]
        else:
            dp[start][end]=min(dp[start][end], dfs(start,index)+dfs(index+1,end)+arr[start][0]*arr[index][1]*arr[end][1])
        
    return dp[start][end]
print(dfs(0,n-1))