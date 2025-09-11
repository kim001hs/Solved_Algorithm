import sys
input=sys.stdin.readline
n=int(input())
arr=[]
index=0
for i in range(n):
    tmp=input().split()
    if tmp[0]=="push":
        arr.append(tmp[1])
    elif tmp[0]=="pop":
        if index==len(arr):
            print(-1)
        else:
            print(arr[index])
            index+=1
    elif tmp[0]=="size":
        print(len(arr)-index)
    elif tmp[0]=="empty":
        if index==len(arr):
            print(1)
        else:
            print(0)
    elif tmp[0]=="front":
        if index==len(arr):
            print(-1)
        else:
            print(arr[index])
    else:#back
        if index==len(arr):
            print(-1)
        else:
            print(arr[-1])