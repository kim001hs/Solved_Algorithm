import sys
def input(): return sys.stdin.readline().rstrip()
n= int(input())
arr=list(map(int,input().split()))
arr+=[0,0]
result=0
for i in range(n):
    if arr[i+1]>arr[i+2]:
        #2개 먼저삼 뒤에 합칠거는 남겨놓음
        low=min(arr[i],arr[i+1]-arr[i+2])
        result+=5*low
        arr[i]-=low;arr[i+1]-=low
        #남으면 3개짜리 삼
        low=min(arr[i],arr[i+1],arr[i+2])
        result+=7*low
        arr[i]-=low;arr[i+1]-=low;arr[i+2]-=low
    else:
        #3개짜리 삼
        low=min(arr[i],arr[i+1],arr[i+2])
        result+=7*low
        arr[i]-=low;arr[i+1]-=low;arr[i+2]-=low
    #남은건 1개짜리로 삼
    result+=3*arr[i]
print(result)