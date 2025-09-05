import sys

input = sys.stdin.readline  # 편하게 input()처럼 사용
n= int(input())

for i in range (1,10):
    print(str(n) +' * ' + str(i) + ' = ' + str(n*i))

