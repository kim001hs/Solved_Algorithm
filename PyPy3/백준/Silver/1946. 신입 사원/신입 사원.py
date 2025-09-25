import sys
def input(): return sys.stdin.readline().rstrip()
t=int(input())
for _ in range(t):
    n=int(input())
    ipt=[]
    result=[]
    for i in range(n):
        a,b=map(int, input().split())
        ipt.append((a,b))
    ipt.sort()
    result.append(ipt[0])
    for i in ipt:
        if i[1]<result[-1][1]:
            result.append(i)
    print(len(result))