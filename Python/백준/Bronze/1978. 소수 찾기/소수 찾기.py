import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
result=0
for i in arr:
    is_break=False
    if(i<2):
        continue
    for j in range(2,i):
        if(i%j==0):
            is_break=True
            break
    if(is_break==False):
        result+=1
print(result)