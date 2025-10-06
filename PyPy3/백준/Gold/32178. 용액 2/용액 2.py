import sys
def input(): return sys.stdin.readline().rstrip()
INF=int(1e10)
n=int(input())
arr=[0]+list(map(int,input().split()))
min_=INF
for i in range(1,n+1):#부분합 배열로 만들기
    arr[i]+=arr[i-1]
ID=[i for i in range(n+1)]
ID.sort(key=lambda x:arr[x])#부분합 배열 기준으로 인덱스 배열을 정렬

res=int(2*1e9)

for i in range(n):
    a,b=ID[i],ID[i+1]
    if arr[b]-arr[a]<abs(res):
        res=arr[b]-arr[a]
        if a<=b:
            left,right=a+1,b
        else:
            left,right=b+1,a
            res*=-1

print(res)
print(left,right)