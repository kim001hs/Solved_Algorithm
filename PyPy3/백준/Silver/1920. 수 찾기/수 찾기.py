import sys
input=sys.stdin.readline
n=int(input())
list_=list(map(int, input().split()))
m=int(input())
arr=list(map(int, input().split()))
list_.sort()
def find(i):

    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if i == list_[mid]:
            return 1
        elif i > list_[mid]:
            left=mid+1
        else:
            right=mid-1
    return 0
for i in arr:
    print(find(i))