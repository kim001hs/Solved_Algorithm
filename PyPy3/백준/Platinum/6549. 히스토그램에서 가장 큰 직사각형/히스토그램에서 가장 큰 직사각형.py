import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
result=[]
while True:
    histo=list(map(int, input().split()))
    if histo[0]==0:
        break
    stack=[]
    n=histo[0]
    max_=0
    for i in range(1,n+1):
        if not stack:
            stack.append((i,histo[i]))
        else:
            if stack[-1][1]<=histo[i]:
                stack.append((i,histo[i]))
            else:
                while stack and stack[-1][1] > histo[i]:#작은건 냅두기 벽으로 사용
                    prev=stack.pop()
                    if stack:
                        width=i-stack[-1][0]-1#스택의 제일 위로 계산
                    else:
                        width=i-1#스택이 비었으면 i-1이 너비
                    max_=max(max_,width*prev[1])
                stack.append((i,histo[i]))
    while stack:#마지막에 계속 올라가면 계산이 안되니까 한번 더 
        prev=stack.pop()
        if stack:
            width=n-stack[-1][0]
        else:
            width=n
        max_=max(max_,width*prev[1])
    print(max_)