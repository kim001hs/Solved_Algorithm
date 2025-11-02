import sys


def input():
    return sys.stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    a = x1 * y2 + x2 * y3 + x3 * y1
    b = y1 * x2 + y2 * x3 + y3 * x1
    return a - b

def print_point(ax, ay, bx, by, cx, cy, dx, dy):
    #겹치는 점이 하나일 때 호출되므로 선분이 아닌 직선으로 생각
    # 직선 AB: (bx-ax)*(y - ay) = (by-ay)*(x - ax)
    # 직선 CD: (dx-cx)*(y - cy) = (dy-cy)*(x - cx)

    # 계수 계산
    A1 = by - ay
    B1 = ax - bx
    C1 = A1 * ax + B1 * ay

    A2 = dy - cy
    B2 = cx - dx
    C2 = A2 * cx + B2 * cy

    det = A1 * B2 - A2 * B1

    # 교점 좌표
    x = (B2 * C1 - B1 * C2) / det
    y = (A1 * C2 - A2 * C1) / det
    print(f"{x:.9f} {y:.9f}")
    return

ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

abc = ccw(ax, ay, bx, by, cx, cy)
abd = ccw(ax, ay, bx, by, dx, dy)
cda = ccw(cx, cy, dx, dy, ax, ay)
cdb = ccw(cx, cy, dx, dy, bx, by)

if (abc * abd < 0) and (cda * cdb < 0):
    print(1)
    print_point(ax, ay, bx, by, cx, cy, dx, dy)
elif abc == abd == 0:# 두 선분이 일직선
    if max(ax, bx) >= min(cx, dx) and (min(ax, bx) <= max(cx, dx)) and max(ay, by) >= min(cy, dy) and min(ay, by) <= max(cy, dy):
    #일직선이교 겹칠 때
        print(1)
        if ax != bx:  # 수직선이 아닐 때
            if ax > bx:
                right_ab, left_ab = (ax, ay), (bx, by)
            else:
                right_ab, left_ab = (bx, by), (ax, ay)

            if cx < dx:
                left_cd, right_cd = (cx, cy), (dx, dy)
            else:
                left_cd, right_cd = (dx, dy), (cx, cy)

            if right_ab == left_cd:
                print(right_ab[0], right_ab[1])
            elif left_ab == right_cd:
                print(left_ab[0], left_ab[1])
        else:  # 수직선
            if ay > by:
                top_ab, bottom_ab = (ax, ay), (bx, by)
            else:
                top_ab, bottom_ab = (bx, by), (ax, ay)

            if cy < dy:
                bottom_cd, top_cd = (cx, cy), (dx, dy)
            else:
                bottom_cd, top_cd = (dx, dy), (cx, cy)

            if top_ab == bottom_cd:
                print(top_ab[0], top_ab[1])
            elif bottom_ab == top_cd:
                print(bottom_ab[0], bottom_ab[1])
    else:#일직선인데 겹치지 않을 때
        print(0)
elif (abc * abd == 0 and cda * cdb <= 0) or (abc * abd <= 0 and cda * cdb == 0):# 한 점이 다른 선분 위에 있을 때
    print(1)
    print_point(ax, ay, bx, by, cx, cy, dx, dy)
else:
    print(0)