from heapq import heappush,heappop,heapify
import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
result=[0]*n
arr=list(map(int,input().split()))
stack=[]
result=[]
for i in range(n):
    temp=arr[i]
    while len(stack)!=0 and arr[stack[-1]]<temp:
        stack.pop()
    if len(stack)!=0:
        result.append(stack[-1]+1)
    else:
        result.append(0)
    heappush(stack,i)
for i in result:
    print(i,end=" ")