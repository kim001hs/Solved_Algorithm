import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    temp=str(input().rstrip())
    is_vps=0
    flag=False
    for j in temp:
        if j=='(':
            is_vps+=1
        else:
            is_vps-=1
        if is_vps<0:
            print("NO")
            flag=True
            break
    if flag==False:
        if is_vps:
            print("NO")
        else:
            print("YES")