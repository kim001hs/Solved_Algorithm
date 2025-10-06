import sys
def input(): return sys.stdin.readline().rstrip()
p1x,p1y=map(int, input().split())
p2x,p2y=map(int, input().split())
p3x,p3y=map(int, input().split())

ccw=(p2x-p1x)*(p3y-p1y)-(p3x-p1x)*(p2y-p1y)
if ccw>0:
    print(1)
elif ccw<0:
    print(-1)
else:
    print(0)