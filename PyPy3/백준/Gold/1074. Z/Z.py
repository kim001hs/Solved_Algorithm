import sys
input = sys.stdin.readline
N,r,c=list(map(int, input().split()))
n=2
while(r>=n or c>=n):
    n*=2
    
r+=1
c+=1
n//=2
res=0

while(n>=1):
    if r>n and c>n:
        res+=3*n*n
        r-=n
        c-=n
    elif r>n:
        res+=2*n*n
        r-=n
    elif c>n:
        res+=n*n
        c-=n
    n//=2
    
print(res)