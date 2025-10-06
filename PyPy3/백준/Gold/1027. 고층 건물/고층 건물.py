import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=list(map(int,input().split()))
result=0
for i in range(n):
    left_slope=-1000000000
    right_slope=-1000000000
    count=0
    for j in range(1,n):
        if i-j<0:
            break
        slope=(arr[i-j]-arr[i])/j
        if slope>left_slope:
            left_slope=slope
            count+=1
    for j in range(1,n):
        if i+j>n-1:
            break
        slope=(arr[i+j]-arr[i])/j
        if slope>right_slope:
            right_slope=slope
            count+=1
    result=max(result,count)
print(result)