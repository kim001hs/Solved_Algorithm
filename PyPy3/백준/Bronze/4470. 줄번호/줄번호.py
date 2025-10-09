import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
for i in range(n):
    temp=input()
    print(str(i+1)+". "+temp)