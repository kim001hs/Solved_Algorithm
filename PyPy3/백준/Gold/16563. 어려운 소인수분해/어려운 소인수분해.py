import sys


def input(): return sys.stdin.readline().rstrip()


def steve():
    # 1000까지
    global isPrime
    for i in range(2, 2237):
        if isPrime[i]:
            for j in range(i*i, 5000001, i):
                if isPrime[j] == j:#가장 작은 소인수를 넣어줌
                    isPrime[j] = i
    return

isPrime = [i for i in range(5000001)]
steve()
t = int(input())
arr = list(map(int, input().split()))
for n in arr:
    res = []
    while(n>1):
        res.append(isPrime[n])
        n//=isPrime[n]
    print(*res)
