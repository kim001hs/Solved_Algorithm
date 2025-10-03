import sys
def input(): return sys.stdin.readline().rstrip()
n,m=map(int, input().split())
print(n//m)
print(n%m)