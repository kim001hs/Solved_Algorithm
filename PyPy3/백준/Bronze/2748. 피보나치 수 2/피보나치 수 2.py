import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
fibo=[1,1]
for i in range(2,n):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[n-1])