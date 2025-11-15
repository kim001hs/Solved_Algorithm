import sys


def input(): return sys.stdin.readline().rstrip()


a, b = map(int, input().split())
print(min(a, b)//2)