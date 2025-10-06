import sys
def input(): return sys.stdin.readline().rstrip()
p1x,p1y,p1r=map(int, input().split())
p2x,p2y,p2r=map(int, input().split())
if (p1r+p2r)**2>(p1x-p2x)**2+(p1y-p2y)**2:
    print("YES")
else:
    print("NO")