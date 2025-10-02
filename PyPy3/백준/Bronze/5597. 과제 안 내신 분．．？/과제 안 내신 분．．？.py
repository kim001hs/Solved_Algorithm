import sys
def input(): return sys.stdin.readline().rstrip()
arr=[False]*30
for i in range(28):
    n=int(input())
    arr[n-1]=True
for i in range(30):
    if arr[i]==False:
        print(i+1)