from heapq import heappush,heappop,heapify
import sys
def input(): return sys.stdin.readline().rstrip()
INF=2000000001
n=int(input())
arr=list(map(int,input().split()))
closest=[]
min_=INF
arr.sort()
start=0
end=n-1
while(start<end):
    sum_=arr[start]+arr[end]
    if abs(sum_)<min_:
        min_=abs(sum_)
        closest=[arr[start],arr[end]]
    if sum_<0:
        start+=1
    else: 
        end-=1
print(str(closest[0])+' '+str(closest[1]))