from heapq import heapify,heappop,heappush
import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
small=[]
big=[]
for i in range(n):
    temp=int(input())
    if not i%2:
        heappush(big, temp)
        heappush(small, -heappop(big))
    else:
        heappush(small, -temp)
        heappush(big, -heappop(small))
    print(-small[0])