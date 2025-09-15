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
                while stack and stack[-1][1] > histo[i]:
                    prev=stack.pop()
                    if stack:
                        width=i-stack[-1][0]-1
                    else:
                        width=i-1
                    max_=max(max_,width*prev[1])
                stack.append((i,histo[i]))
    while stack:
        prev=stack.pop()
        if stack:
            width=n-stack[-1][0]
        else:
            width=n
        max_=max(max_,width*prev[1])
    print(max_)