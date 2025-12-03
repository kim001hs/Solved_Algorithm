import sys


def input(): return sys.stdin.readline().rstrip()


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    gcd_ = gcd(a, b)
    if c % gcd_ or max(a, b) < c:
        print("NO")
    else:
        print("YES")
