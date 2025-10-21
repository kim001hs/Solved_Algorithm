import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
for i in range(n):
    arr=list(map(str,input().split()))
    for string in arr:
        print(string[::-1],end=' ')