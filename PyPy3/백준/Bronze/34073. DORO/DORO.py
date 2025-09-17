import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
arr=list(map(str, input().split()))
for i in range(N):
    print(arr[i]+"DORO",end=' ')