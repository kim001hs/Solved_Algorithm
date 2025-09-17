import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
N=int(input())
for i in range(N):
    arr=list(map(int, input().split()))
    arr.sort()
    if arr[3]-arr[1]>=4:
        print("KIN")
    else:
        print(arr[1]+arr[2]+arr[3])