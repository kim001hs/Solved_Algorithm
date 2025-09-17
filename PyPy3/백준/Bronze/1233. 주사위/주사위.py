import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
s1,s2,s3=map(int, input().split())
arr=[0]*(s1+s2+s3-2)
for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            arr[i+j+k]+=1
max_=0
sum_=0
for i in range(s1+s2+s3-3):
    if max_<arr[i]:
        max_=arr[i]
        sum_=i+3
print(sum_)