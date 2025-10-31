import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
closest=[]
min_=int(1e12)
for i in range(n-2):
    start,end=i+1,n-1
    while(start<end):
        sum_=arr[i]+arr[start]+arr[end]
        if abs(sum_)<min_:
            min_=abs(sum_)
            closest=(i,start,end)
        if sum_==0:
            break
        if sum_<0:
            start+=1
        else:
            end-=1
print(arr[closest[0]],arr[closest[1]],arr[closest[2]])