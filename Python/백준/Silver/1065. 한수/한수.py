import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용

N= int(input())
count=0
for i in range(1,N+1):
    if(i>=10):
        a=(i//10)%10-i%10
    else:
        count+=1
        continue
    if(i>=100):
        b=(i//100)%10-(i//10)%10
        if(b!=a):
            continue
    else:
        count+=1
        continue
    if(i>=1000):
        b=i//1000-(i//100)%10
        if(b!=a):
            continue
    else:
        count+=1
print(count)