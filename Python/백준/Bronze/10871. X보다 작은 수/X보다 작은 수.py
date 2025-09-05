import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용

N,X=map(int,input().split())
arr=list(map(int,input().split()))
for i in arr:
    if(i<X):
        print(i, end=' ')
