import sys
input = sys.stdin.readline
A,B,V=map(int,input().split())
oneday=A-B
result = (V - A) // oneday + 1 if (V - A) % oneday==0 else (V - A) // oneday +2
print(result)
