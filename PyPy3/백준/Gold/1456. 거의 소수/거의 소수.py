import sys
from math import sqrt, ceil


def input(): return sys.stdin.readline().rstrip()


def steve(b):
    # 10^7까지
    isPrime[0], isPrime[1] = 0, 0
    for i in range(2, int(b ** 0.5)):
        if isPrime[i]:
            for j in range(i*i, 10**7+1, i):
                isPrime[j] = False
    return


def count_steve(a, b):
    count = 0
    for i in range(2, 10**7 + 1):
        if isPrime[i]:
            j = 2
            while i ** j <= b:
                if i ** j >= a:
                    count += 1
                j += 1
    return count


isPrime = [True]*(10**7+1)
a, b = list(map(int, input().split()))
steve(b)
print(count_steve(a, b))
