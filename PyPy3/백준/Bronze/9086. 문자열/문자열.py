import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
for i in range(n):
    string=input()
    print(string[0]+string[-1])