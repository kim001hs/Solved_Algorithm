import sys
from math import sqrt, ceil


def input(): return sys.stdin.readline().rstrip()


def steve(k):
    global isPrime
    isPrime[0], isPrime[1] = False, False
    for i in range(2, k):
        if isPrime[i] == True:
            for j in range(i*i, k, i):
                isPrime[j] = False
    return


m = int(ceil(sqrt(50000))+1)
isPrime = [True]*(m)
steve(int(ceil(sqrt(m))+1))
k = int(input())
res = 0
for n in range(2, k+1):
    m = int(ceil(sqrt(n)+1))
    phi = 1
    for i in range(2, m):
        if isPrime[i]:
            count = 0
            while not n % i:
                count += 1
                n //= i
            if count:
                phi *= pow(i, count)-pow(i, count-1)
    if n != 1:
        phi *= (n-1)
    res += phi
print(res)