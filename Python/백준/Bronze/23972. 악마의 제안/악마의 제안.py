import sys
def input(): return sys.stdin.readline().rstrip()
n, m = map(int, input().split())
if m <= 1:
    res=-1
elif n*m % (m-1) != 0:
    res=n*m//(m-1)+1
else:
    res=n*m//(m-1)
print(res)