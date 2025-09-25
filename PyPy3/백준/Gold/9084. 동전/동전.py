import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
#동전 1만 사용>2도>3도...
for _ in range(n):
    i=int(input())
    coins=list(map(int,input().split()))
    price=int(input())
    dp=[0]*(price+1)
    dp[0]=1
    for coin in coins:
        for i in range(1,price+1):
            if i-coin>=0 and dp[i-coin]!=0:
                dp[i]+=dp[i-coin]
    print(dp[price])