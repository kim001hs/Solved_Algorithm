import sys
def input(): return sys.stdin.readline().rstrip()
n,m=map(int, input().split())
arr=list(map(int,input().split()))
sum_=[0]
for i in range(n):
    sum_.append(sum_[-1]+arr[i])
for i in range(m):
    a,b=map(int, input().split())
    print(sum_[b]-sum_[a-1])