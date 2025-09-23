from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
n,m=map(int, input().split())
arr=[]
rotate=[[1,0],[0,1],[-1,0],[0,-1]]
max_h=0
needcount=0
for i in range(n):
    data=list(map(int, input().split()))
    for idx,j in enumerate(data):
        if j>0:
            needcount+=1
            next_i,next_j=i,idx
    arr.append(data)
total=0

def bfs(i,j,needcount):
    #1씩 빼면서 다음번에 살아있는 빙산 수 저장
    #시작점에서 bfs하면서 카운트
    nxi,nxj=i,j
    global arr
    count=1
    visited=[[False]*m for _ in range(n)]
    queue=deque()
    queue.append((i,j))
    visited[i][j]=True
    if arr[i][j]==0:
        return 0,0,0,0
    while queue:
        i,j=queue.popleft()
        for k in range(4):
            ni,nj=i+rotate[k][0],j+rotate[k][1]
            if 0<=ni<n and 0<=nj<m and visited[ni][nj]==False:
                if arr[ni][nj]>0:
                    visited[ni][nj]=True
                    queue.append((ni,nj))
                    count+=1
                else:   
                    arr[i][j]-=1
                    if arr[i][j]==0:
                        needcount-=1
        if arr[i][j]>0:
            nxi,nxj=i,j
    return count, needcount,nxi,nxj

while True:
    count,temp,next_i,next_j=bfs(next_i,next_j,needcount)
    if temp<=0:
        print(0)
        break
    if count!=needcount:
        print(total)
        break
    needcount=temp
    total+=1