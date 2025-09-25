import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
rotate=[[1,0],[0,1],[-1,0],[0,-1]]
for _ in range(n):
    temp=list(str(input()))
    arr.append(temp)

def bfs(x,y):
    global arr
    count=0
    queue=deque()
    queue.append((x,y))
    while queue:
        i,j=queue.popleft()
        if arr[i][j]=='0':
            continue
        arr[i][j]='0'
        count+=1
        for k in range(4):
            ni, nj=i+rotate[k][0], j+rotate[k][1]
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]=='1':
                queue.append((ni,nj))
    return count

ans=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]=='0':
            continue
        ans.append(bfs(i,j))
ans.sort()
print(len(ans))
print(*ans, sep='\n')