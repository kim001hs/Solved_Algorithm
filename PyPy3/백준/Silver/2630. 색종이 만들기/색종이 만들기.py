import sys
input = sys.stdin.readline
n=int(input())
array=[]
blue=0
white=0
for i in range(n):
    data=list(map(int, input().split()))
    array.append(data)

def solve(arr,N):
    global blue,white
    count=0
    for row in arr:
        for i in row:
            count+=i
    if count==0:
        white+=1
        return
    elif count==len(arr)**2:
        blue+=1
        return
    for i in range(0,N,N//2):
        for j in range(0,N,N//2):
            solve([row[i:i+N//2] for row in arr[j:j+N//2]],N//2)
solve(array,n)
print(white)
print(blue)