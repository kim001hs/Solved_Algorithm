from heapq import heappush,heappop,heapify
import sys
def input(): return sys.stdin.readline().rstrip()
INF=(1e9)
N,C=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort()
def installNum(len):
    count=1
    temp=arr[0]
    for i in arr:
        if i-temp>=len:
            temp=i
            count+=1
    return count
start=1
end=arr[N-1]
while(start<=end):
    mid=(start+end)//2
    if installNum(mid)>=C:
        start=mid+1
    elif installNum(mid)<C:
        end=mid-1                   
print(start-1)