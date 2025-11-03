import sys
from math import sqrt, ceil


def input(): return sys.stdin.readline().rstrip()


def steve(m):
    global isPrime
    isPrime[0], isPrime[1] = False, False
    for i in range(2, m):
        if isPrime[i] == True:
            for j in range(i*i, m, i):
                isPrime[j] = False
    return


def oiler_phi(n):
    phi = 1
    for i in range(2, m):
        if isPrime[i]:
            count = 0
            while not n % i:#i가 n의 약수면 i로 계속 나눠서 없애줌
                count += 1
                n = n//i
            if count:#count==0일때 1이 곱해져서 없어도 됨
                phi *= int(pow(i, count))-int(pow(i, count-1))
    if n != 1:
        phi *= n-1
    return phi


n = int(input())
m = int(ceil(sqrt(n))+1)
isPrime = [True]*(m)
print(oiler_phi(n))