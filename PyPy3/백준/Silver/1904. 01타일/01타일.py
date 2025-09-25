import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
#1은 하나 가능 0은 00만 가능
t1,t2=1,2
temp=1 if n==1 else 2
for i in range(2,n):
    temp=(t1+t2)%15746
    t1,t2=t2,temp
print(temp)