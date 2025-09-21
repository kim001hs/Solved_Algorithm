import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=deque(map(int, input().split()))
count=list(map(int, input().split()))
INF=int(1e9)
def dfs(arr1, count1):
    max_=-INF
    min_=INF
    if len(arr1)==1:
        return arr1[0], arr1[0]
    for i in range(4):
        if count1[i]!=0:
            count2=count1[:]
            count2[i]-=1
            arr2=deque(arr1)
            x=arr2.popleft()
            y=arr2.popleft()
            if x==6 and y==4 and i==3:
                dsf=32
            if i==0:
                x+=y
            elif i==1:
                x-=y
            elif i==2:
                x*=y
            else:
                x=int(x / y)
            arr2.appendleft(x)
            mx,mn=dfs(arr2, count2)
            max_=max(max_,mx)
            min_=min(min_,mn)
    return max_,min_

mxx,mnn=dfs(arr, count)
print(mxx)
print(mnn)