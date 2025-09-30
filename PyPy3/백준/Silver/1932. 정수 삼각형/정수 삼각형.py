import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
if n!=0:
    prev=list(map(int, input().split()))
cur=[prev[0]]
for i in range(2,n+1):
    data=list(map(int, input().split()))
    cur=[prev[0]+data[0]]
    for j in range(1,i-1):
        temp=max(prev[j-1],prev[j])
        cur.append(temp+data[j])
    cur.append(prev[-1]+data[-1])
    prev=cur
print(max(cur))