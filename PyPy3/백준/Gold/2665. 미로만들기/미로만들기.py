import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=int(input())
miro=[]
gogo=[[1,0],[0,1],[-1,0],[0,-1]]
for _ in range(n):
    data=input()
    miro.append(data)
def dfs():
    visited=[[False]*n for _ in range(n)]
    dq=deque()
    dq.append((0,0,0))
    while dq:
        i,j,count=dq.popleft()
        for k in range(4):
            ni,nj=i+gogo[k][0],j+gogo[k][1]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==False:
                if ni==n-1 and nj==n-1:
                    return count
                if miro[ni][nj]=='1':
                    dq.appendleft((ni,nj,count))
                    visited[ni][nj]=True
                else:
                    dq.append((ni,nj,count+1))
                    visited[ni][nj]=True
print(dfs())