import sys
from math import sqrt


def input(): return sys.stdin.readline().rstrip()


a, b = map(int, input().split())
isNONO = [True] * (b - a + 1)
limit = int(sqrt(b))
for i in range(2, limit + 1):
    temp = i**2
    start = ((a + temp - 1) // temp) * temp  # a를 i*i의 배수로 올림
    for j in range(start, b+1, temp):
        isNONO[j-a] = False
print(sum(isNONO))
