import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
arr=[]
for i in range(9):
    temp=int(input())
    arr.append(temp)
max=0
maxIndex=0
for i in range(len(arr)):
    if(arr[i]>max):
        max=arr[i]
        maxIndex=i+1
print(max)
print(maxIndex)
