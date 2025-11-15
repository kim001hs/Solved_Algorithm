import sys


def input(): return sys.stdin.readline().rstrip()


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(max(sum(arr1), sum(arr2)))