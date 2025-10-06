import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
x,y=[],[]#x와 y좌표를 저장하는 리스트
for i in range(n):
    x1,y1=map(int,input().split())
    x.append(x1)
    y.append(y1)
sumA,sumB=0,0#신발끈 공식 x1y2...와 x2y1...의 합
for i in range(n):
    sumA+=x[i]*y[(i+1)%n]
    sumB+=x[(i+1)%n]*y[i]
print(abs(sumA-sumB)/2)