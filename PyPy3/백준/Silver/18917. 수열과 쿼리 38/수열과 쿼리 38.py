import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
M=int(input())
sum_=0
xor_=0
for i in range(M):
    temp=list(map(int, input().split()))
    if temp[0]==1:
        sum_+=temp[1]
        xor_^=temp[1]
    elif temp[0]==2:
        sum_-=temp[1]
        xor_^=temp[1]
    elif temp[0]==3:
        print(sum_)
    else:
        print(xor_)