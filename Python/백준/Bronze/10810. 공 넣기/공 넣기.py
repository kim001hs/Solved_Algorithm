n,m=map(int,input().split())
arr=[0]*n
for _ in range(m):
    s,e,num=map(int,input().split())
    for i in range(s-1,e):
        arr[i]=num
print(*arr)