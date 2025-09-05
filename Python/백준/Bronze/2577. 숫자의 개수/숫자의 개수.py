import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
a=int(input())
b=int(input())
c=int(input())
result=a*b*c
arr=[0]*10
for i in str(result):
    arr[int(i)]+=1
for i in arr:
    print(i)
    