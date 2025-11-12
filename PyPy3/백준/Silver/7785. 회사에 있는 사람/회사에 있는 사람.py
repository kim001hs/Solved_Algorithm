import sys

def input(): return sys.stdin.readline().rstrip()


n = int(input())
arr = {}
for i in range(n):
    t1, t2 = map(str, input().split())
    if t2 == "enter":
        arr[t1] = 1
    else:
        del arr[t1]
arr = list(arr.keys())
arr.sort(reverse=True)
for i in arr:
    print(i)