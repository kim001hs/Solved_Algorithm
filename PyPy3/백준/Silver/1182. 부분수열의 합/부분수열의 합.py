import sys
input=sys.stdin.readline
N,S=map(int, input().split())
arr=list(map(int, input().split()))

def solve():
    count=0
    for mask in range(1,(1<<N)):
        sum_=0
        for i in range(N):
            if mask & (1<<i):
                sum_+=arr[i]
        if sum_==S:
            count+=1
    return count

print(solve())