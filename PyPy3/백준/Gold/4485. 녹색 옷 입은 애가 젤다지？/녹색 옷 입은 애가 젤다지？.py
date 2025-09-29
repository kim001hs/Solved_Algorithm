import sys
import heapq
input = sys.stdin.readline
INF=int(1e9)
di=[1,0,-1,0]
dj=[0,1,0,-1]
seq=0
while True:
    seq+=1
    n=int(input())
    if n==0:
        break
    arr=[]
    for i in range(n):
        data=list(map(int, input().split()))
        arr.append(data)
    pq=[]
    pq.append((arr[0][0],0,0))
    dist=[[INF]*n for _ in range(n)]
    while pq:
        temp,i,j=heapq.heappop(pq)
        if dist[i][j]<=temp:
            continue
        dist[i][j]=temp
        for k in range(4):
            ni,nj=i+di[k],j+dj[k]
            if 0<=ni<n and 0<=nj<n and dist[ni][nj]>arr[i][j]+arr[ni][nj]:
                heapq.heappush(pq, (dist[i][j]+arr[ni][nj],ni,nj))
    print("Problem "+str(seq)+": "+str(dist[n-1][n-1]))