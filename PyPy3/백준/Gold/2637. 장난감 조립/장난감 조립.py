from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
M=int(input())
graph=[[] for _ in range(N)]
gnum=[0]*N#남은 필요조건 수
min_=int(1e9)
for i in range(M):
    X,Y,K=map(int,input().split())
    graph[Y-1].append([X-1,K])
    gnum[X-1]+=1
def topology_sort():#위상정렬
    result=[{} for _ in range(N)]
    queue=deque()
    for i in range(N):#먼저 필요조건이 0인 것들을 넣어줌
        if gnum[i]==0:
            queue.append(i)
            result[i][i]=1
    while queue:#꺼내서 확인하고 이어진 간선에 gnum은 1을 빼고 result는 1 더해줌
        temp=queue.popleft()
        for j in graph[temp]:
            i=j[0]
            gnum[i]-=1
            for k in result[temp]:
                if k in result[i]:
                    result[i][k]+=result[temp][k]*j[1]
                else:
                    result[i][k]=result[temp][k]*j[1]
            if gnum[i]==0:
                queue.append(i)
    return result
res=topology_sort()[N-1]
# res.sort(key=lambda x: list(x.keys())[0])
for i in sorted(res.keys()):
    print(str(i+1)+' '+str(res[i]))