import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,k=map(int,input().split())
arr=[]
location=[[] for _ in range(k)]
rotate=[[1,0],[0,1],[-1,0],[0,-1]]
for _ in range(n):
    temp=list(map(int, input().split()))
    for idx,i in enumerate(temp):
        if i!=0:
            location[i-1].append((_,idx,0))
    arr.append(temp)
s,x,y=map(int,input().split())
queue=deque()
for row in location:
    for i in row:
        queue.append(i)

def bfs():
    global queue
    while queue:
        i,j,count=queue.popleft()
        if count == s:
            break
        for k in range(4):
            ni, nj=i+rotate[k][0], j+rotate[k][1]
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0:
                arr[ni][nj]=arr[i][j]
                if count<s-1:
                    queue.append((ni,nj,count+1))
    return arr[x-1][y-1]

print(bfs())