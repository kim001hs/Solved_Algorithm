import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
di=[1,0,-1,0]
dj=[0,1,0,-1]
mapp=[]
for i in range(n):
    mapp.append(input())
queue=deque()
queue.append((0,0,1,False))#행,열,벽 부쉈는지 여부
visited1=[[False]*m for _ in range(n)]#벽 안부순 visited
visited2=[[False]*m for _ in range(n)]#벽 부순 visited
visited1[0][0],visited2[0][0]=True,True
while queue:
    i,j,count,isbreak=queue.popleft()
    if i==n-1 and j==m-1:
        print(count)
        sys.exit()
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if ni==4 and nj==3:
            sad=213
        if 0<=ni<n and 0<=nj<m and not visited1[ni][nj]:
            if mapp[ni][nj]=='0':
                if not isbreak or not visited2[ni][nj]:
                    if not isbreak:
                        visited1[ni][nj]=True
                    if ni==n-1 and nj==m-1:
                        print(count+1)
                        sys.exit()
                    queue.append((ni,nj,count+1,isbreak))
            
            elif not isbreak:
                if ni==n-1 and nj==m-1:
                    print(count+1)
                    sys.exit()
                queue.append((ni,nj,count+1,True))
            visited2[ni][nj]=True
print(-1)