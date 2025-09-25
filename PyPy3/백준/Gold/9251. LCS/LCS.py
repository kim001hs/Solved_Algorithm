import sys
def input(): return sys.stdin.readline().rstrip()
s='a'+str(input().rstrip())
t='a'+str(input().rstrip())
len_s,len_t=len(s),len(t)
dp=[[0]*(len_s+1) for _ in range(len_t+1)]
for i in range(1,len_t):
    for j in range(1,len_s):
        if s[j]==t[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[len_t-1][len_s-1])