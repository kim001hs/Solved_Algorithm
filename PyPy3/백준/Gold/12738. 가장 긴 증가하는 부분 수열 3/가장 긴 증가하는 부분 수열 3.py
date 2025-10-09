import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))

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
print(len(res))