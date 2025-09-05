import sys

input = sys.stdin.readline  # 편하게 input()처럼 사용
n= int(input())

for i in range (1,n+1):
    stars=""
    for k in range (i):
        stars+="*"
    print(stars)