import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    tmp=input().split()
    if tmp[0]=="push":
        arr.append(tmp[1])
    elif tmp[0]=="pop":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop()
    elif tmp[0]=="size":
        print(len(arr))
    elif tmp[0]=="empty":
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif tmp[0]=="top":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])