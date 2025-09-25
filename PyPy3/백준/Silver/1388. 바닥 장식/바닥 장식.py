import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n,m=map(int,input().split())
pattern=[]
for _ in range(n):
    temp=list(input())
    pattern.append(temp)
visited=[[False]*m for _ in range(n)]
def fill(i,j):
    global visited
    visited[i][j]=True
    if pattern[i][j]=='-':
        if j<m-1 and pattern[i][j+1]=='-' and visited[i][j+1]==False:
            fill(i,j+1)
    else:
        if i<n-1 and pattern[i+1][j]=='|' and visited[i+1][j]==False:
            fill(i+1,j)                
    return
count=0
for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            else:
                fill(i,j)
                count+=1
print(count)