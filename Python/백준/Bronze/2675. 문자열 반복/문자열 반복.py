import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
T=int(input())
for i in range(T):
    data=input().split()
    n=int(data[0])
    str=data[1]
    result=""
    for j in str:
        for k in range(n):
            result+=j
    print(result)