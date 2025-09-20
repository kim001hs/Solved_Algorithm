import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
def is_bipartite():
    v,e=map(int, input().split())
    graph=[[]for _ in range(v)]
    queue=deque()
    is_black=[None]*v#방문 안했으면 None, 블랙이면 True, 레드면 False
    for i in range(e):
        t1,t2=map(int, input().split())
        graph[t1-1].append(t2-1)
        graph[t2-1].append(t1-1)  
    
    for i in range(v):
        if is_black[i]!=None:
            continue
        else:
            is_black[i]=True#그냥 블랙으로 처리
            queue.append(i)
            while queue:
                temp=queue.popleft()
                for j in graph[temp]:
                    if is_black[j]==None:
                        is_black[j]=not is_black[temp]
                        queue.append(j)
                    elif is_black[j]==is_black[temp]:
                        return "NO"
    return "YES"

n=int(input())
for _ in range(n):
    print(is_bipartite())