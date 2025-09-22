import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
miro=[]
visited=[[False]*m for _ in range(n)]
gogogo=[[1,0],[0,1],[-1,0],[0,-1]]
for i in range(n):
    data=input()
    miro.append(data)
def bfs():
    queue=deque()
    queue.append((0,0,0))
    visited[0][0]=True
    while queue:
        i,j,count=queue.popleft()
        for k in range(4):
            ni=i+gogogo[k][0]
            nj=j+gogogo[k][1]
            if ni==n-1 and nj==m-1:
                return count+2
            if 0<=ni<n and 0<=nj<m and miro[ni][nj]=='1' and visited[ni][nj]==False:
                queue.append((ni,nj,count+1))
                visited[ni][nj]=True

print(bfs())