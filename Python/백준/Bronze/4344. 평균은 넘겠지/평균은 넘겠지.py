import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
C=int(input())
for i in range(C):
    data = list(map(float, input().split()))
    N = data[0]
    scores = data[1:]
    avg=sum(scores)/N
    num=float(0)
    for j in scores:
        if(j>avg):
            num+=1
    rate=num/N*100
    print(f'{rate:.3f}%')