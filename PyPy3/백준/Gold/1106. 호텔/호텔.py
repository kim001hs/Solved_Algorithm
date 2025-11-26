import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


INF = int(1e9)
c, n = map(int, input().split())
dp = [INF]*(c+1)
dp[0] = 0
for _ in range(n):
    cost, people = map(int, input().split())
    for i in range(1, c+1):
        dp[i] = min(dp[i], cost+(dp[i-people] if i >= people else dp[0]))
print(dp[c])