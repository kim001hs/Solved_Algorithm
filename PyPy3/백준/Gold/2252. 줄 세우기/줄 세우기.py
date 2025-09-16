from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
gnum=[0]*N#남은 필요조건 수
for i in range(M):
    t1,t2=map(int,input().split())
    graph[t1-1].append(t2-1)
    gnum[t2-1]+=1
    
def topology_sort():#위상정렬
    result=[]
    queue=deque()
    for i in range(N):#먼저 필요조건이 0인 것들을 넣어줌
        if gnum[i]==0:
            queue.append(i)
    while queue:#꺼내서 확인하고 이어진 간선에 gnum은 1을 빼고 result는 1 더해줌
        temp=queue.popleft()
        result.append(temp+1)
        for i in graph[temp]:
            gnum[i]-=1
            if gnum[i]==0:
                queue.append(i)
    return result
print(*topology_sort())