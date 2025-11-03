import sys
from math import sqrt, ceil
from itertools import combinations


def input(): return sys.stdin.readline().rstrip()


def comprime_range(a, b, q):  # a<=x<=b인 x 중 q와 서로소의 수
    primes = []  # 소인수 리스트
    n = q
    i = 2
    while i * i <= n:
        if n % i == 0:
            primes.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        primes.append(n)
    # 포함-배제
    count = b - a + 1
    for i in range(1, len(primes) + 1):
        for comb in combinations(primes, i):
            mult = 1
            for p in comb:
                mult *= p
            num = b // mult - (a - 1) // mult  # a~b 범위에서 mult의 배수 개수 계산
            if i % 2:
                count -= num
            else:
                count += num
    return count


a, b = map(int, input().split())
res = 2  # 0,1
maxQ = b//a
for q in range(2, maxQ + 1):
    minP = ceil(a/b)
    res += comprime_range(minP, q, q)
print(res)