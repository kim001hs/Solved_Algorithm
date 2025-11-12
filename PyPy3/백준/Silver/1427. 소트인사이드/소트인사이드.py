import sys


def input(): return sys.stdin.readline().rstrip()


n = list(input())
n.sort(reverse=True)
print(*n, sep='')