import sys
input=sys.stdin.readline
n=int(input())
def loop(n):
    count=1
    temp=(n%10)*10+(n//10+n%10)%10 if n>=10 else n*10+n
    while(n!= temp):
        tmp=temp%10
        temp=(temp%10)*10+(temp//10+temp%10)%10
        count+=1
    return count
print(loop(n))