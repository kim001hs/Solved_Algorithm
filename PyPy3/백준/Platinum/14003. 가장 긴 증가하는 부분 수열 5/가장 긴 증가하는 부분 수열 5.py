import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))
memo=[]#res값이 변할때마다 idx,value 저장
def binary_search(arr,val):
    start,end=0,len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if val<=arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return start
res=[]
for i in arr:
    temp=binary_search(res,i)
    if temp==len(res):
        res.append(i)
    else:
        res[temp]=i
    memo.append((temp,i))
answer=[]
len_res=len(res)
temp_idx=len_res-1
for idx,value in reversed(memo):
    if idx==temp_idx:
        answer.append(value)
        temp_idx-=1
print(len_res)
print(*reversed(answer))