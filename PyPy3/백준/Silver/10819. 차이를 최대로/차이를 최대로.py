import sys
input = sys.stdin.readline
n= int(input())
arr2=[0]*n
arr=list(map(int, input().split()))
arr.sort()
result = 0
def cal():
    result=0
    for i in range (n-1):
        result+=abs(arr2[i]-arr2[i+1])
    return result

if n%2==1:
    arr2[0]=arr[n//2]
    arr2[n-1]=arr[n//2-1]
    for i in range(n-2):
        j=i//2
        if i%2==0:
            arr2[i+1]=arr[n-1-j]
        else:
            arr2[i+1]=arr[j]
    result1=cal()
    arr2[n-1]=arr[n//2+1]
    for i in range(n-2):
        j=i//2
        if i%2==0:
            arr2[i+1]=arr[j]
        else:
            arr2[i+1]=arr[n-1-j]
    result2=cal()
    result=max(result1, result2)
else:
    arr2[0]=arr[n//2-1]
    arr2[n-1]=arr[n//2]
    for i in range(n-2):
        j=i//2
        if i%2==0:
            arr2[i+1]=arr[n-1-j]
        else:
            arr2[i+1]=arr[j]
    result=cal()
    
print(result)
