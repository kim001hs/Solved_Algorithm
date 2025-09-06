import sys
input = sys.stdin.readline
n,m= map(int,input().split())
arr=list(map(int, input().split()))
start=1
end=max(arr)
while start<=end:
    mid=(start+end)//2
    height=0#가져갈 수 있는 높이 총합
    for i in arr:
        if(i>mid):
            height+=i-mid
    if height>=m:
        start=mid+1
    else:
        end=mid-1
        
print(end)


