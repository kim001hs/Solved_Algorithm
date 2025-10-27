import sys
import re
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr = list(map(int, re.split(r'[.|:|#]', input())))
print(sum(arr))