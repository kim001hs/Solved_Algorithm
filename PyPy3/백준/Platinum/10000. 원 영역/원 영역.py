import sys
def input(): return sys.stdin.readline().rstrip()
values=[]
n=int(input())
for i in range(n):
    x,r=map(int,input().split())
    values.append(["L", x-r])
    values.append(["R", x+r])
values.sort(key=lambda x:(-x[1],x[0]),reverse=True)#위치기준 동일하면 R이 먼저
#str에 - 붙일 수 없어서 reverse로
stack=[]
count=1
for i in values:
    cum_width=0
    if i[0]=="L":
        stack.append(i)
    else:
        while stack:
            prev=stack.pop()
            if prev[0]=="L":
                width=i[1]-prev[1]
                if width==cum_width:
                    count+=2
                else:
                    count+=1
                stack.append(["C",width])
                break
            else:#prev[0]=="C"
                cum_width+=prev[1]
print(count)