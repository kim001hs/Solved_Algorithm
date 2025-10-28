import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
for _ in range(n):
    mento,mentee=map(str,input().split())
    arr.append((mento,mentee))
arr.sort(key=lambda x:x[1],reverse=True)
arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0],i[1])