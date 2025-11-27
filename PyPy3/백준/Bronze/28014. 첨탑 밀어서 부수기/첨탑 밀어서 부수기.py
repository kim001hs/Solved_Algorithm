n=int(input())
arr=list(map(int,input().split()))
prev=0
count=1
for i in range(n-1):
    if arr[i]<=arr[i+1]:
        count+=1
print(count)