import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
set=set()
for i in range(5):
    temp=int(input())
    if temp in set:
        set.remove(temp)
    else:
        set.add(temp)
print(*set)