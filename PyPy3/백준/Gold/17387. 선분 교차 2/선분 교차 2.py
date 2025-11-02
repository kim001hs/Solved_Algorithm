import sys


def input():
    return sys.stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    a = x1 * y2 + x2 * y3 + x3 * y1
    b = y1 * x2 + y2 * x3 + y3 * x1
    return a - b


ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

abc = ccw(ax, ay, bx, by, cx, cy)
abd = ccw(ax, ay, bx, by, dx, dy)
cda = ccw(cx, cy, dx, dy, ax, ay)
cdb = ccw(cx, cy, dx, dy, bx, by)

if (abc * abd < 0) and (cda * cdb < 0):
    print(1)
elif abc == abd == 0:  # 두 선분이 일직선
    if max(ax, bx) >= min(cx, dx) and (min(ax, bx) <= max(cx, dx)) and \
        max(ay, by) >= min(cy, dy) and min(ay, by) <= max(cy, dy):
        print(1)
    else:
        print(0)
elif (abc * abd == 0 and cda * cdb <= 0) or (abc * abd <= 0 and cda * cdb == 0):  # 한 점이 다른 선분 위에 있을 때
    print(1)
else:
    print(0)
