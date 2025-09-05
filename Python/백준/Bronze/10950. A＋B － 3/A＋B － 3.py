import sys

input = sys.stdin.readline  # 편하게 input()처럼 사용
n= int(input())

for i in range (n):
    a,b=map(int, input().split())
    print(a+b)

