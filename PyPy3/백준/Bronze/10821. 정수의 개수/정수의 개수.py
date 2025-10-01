import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=list(map(int, input().split(sep=',')))
print(len(n))