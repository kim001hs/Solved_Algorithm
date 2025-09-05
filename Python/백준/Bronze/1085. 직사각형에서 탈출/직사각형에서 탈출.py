import sys

input = sys.stdin.readline  # 편하게 input()처럼 사용
x,y,w,h= map(int, input().split())

print(min(x,y,w-x,h-y))