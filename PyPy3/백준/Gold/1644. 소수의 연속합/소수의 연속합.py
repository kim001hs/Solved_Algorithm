import sys
def input(): return sys.stdin.readline().rstrip()
isPrime=[True]*4000001
def steve():
    global isPrime
    for i in range(2,2001):
        if isPrime[i]:
            for j in range(i*i,4000001,i):
                isPrime[j]=False
    
n=int(input())
prime=[]
count,start,end=0,0,0
steve()
for i in range(2,n+1):
    if isPrime[i]:
        prime.append(i)#소수 리스트
length=len(prime)
curSum=0
while True:
    if curSum >= n:
        if curSum == n:
            count += 1
        if start == length:
            break
        curSum -= prime[start]
        start += 1
    else: # curSum < n
        if end == length:
            break
        curSum += prime[end]
        end += 1
print(count)