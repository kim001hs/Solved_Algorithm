import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
n_arr=list(map(int, input().split()))
M=int(input())
m_arr=list(map(int, input().split()))
n_arr.sort()
def binary_search(i):
    start=0
    end=N-1
    while(start<=end):
        mid=(start+end)//2
        if i>n_arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return start

for i in m_arr:
    if binary_search(i)<N and n_arr[binary_search(i)]==i:
        print(1, end=' ')
    else:
        print(0,end=' ')