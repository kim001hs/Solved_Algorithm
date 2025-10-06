import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
num=1#1부터 시작하면 무게추 1이 없을 때 예외처리와 마지막 num+1을 안해도 됨
for i in arr:
    if num<i:#구간이 끊김
        break
    num+=i
print(num)