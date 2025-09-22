import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
r,c=map(int,input().split())
zido=[]
gogo=[[1,0],[0,1],[-1,0],[0,-1]]
dq=deque()
for _ in range(r):
    data=list(input())
    for idx,i in enumerate(data):
        if i=='S':
            dq.append((_,idx,0))
        elif i=='*':
            dq.appendleft((_,idx,0))
    zido.append(data)
def bfs():
    global dq,zido
    while dq:
        i,j,count=dq.popleft()
        for k in range(4):
            ni,nj=i+gogo[k][0],j+gogo[k][1]
            if 0<=ni<r and 0<=nj<c:
                if zido[ni][nj]=='.':
                    if zido[i][j]=='*':
                        zido[ni][nj]='*'
                    else:
                        zido[ni][nj]='S'
                    dq.append((ni,nj,count+1))
                elif zido[ni][nj]=='D' and zido[i][j]=='S':
                    return count+1
    return "KAKTUS"
print(bfs())