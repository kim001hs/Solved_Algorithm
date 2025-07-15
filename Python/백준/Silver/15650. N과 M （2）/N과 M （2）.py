import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
n, m = map(int, input().split())
s=[]
def dfs(idx):
    if len(s) == m:
        print(*s)
        return
    for i in range(idx, n + 1):
        s.append(i)
        dfs(i+1)
        s.pop()
dfs(1)