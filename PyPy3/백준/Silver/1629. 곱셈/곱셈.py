from heapq import heappush,heappop
import sys
A,B,C=map(int,input().split())
result=1
temp=A%C
while(B!=0):
    result*=temp if B%2==1 else 1
    result%=C
    B//=2
    temp=temp**2%C
print(result)