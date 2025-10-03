import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
for i in range(n):
    a,b=map(int, input().split(sep=','))
    print(a+b)