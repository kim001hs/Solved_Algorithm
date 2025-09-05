import sys
input = sys.stdin.readline
arr=[]
n=int(input())
for i in range(n):
    arr.append(input().strip())
arr=list(set(arr))
arr.sort()
arr.sort(key=len)
for i in range(len(arr)):
    print(arr[i])