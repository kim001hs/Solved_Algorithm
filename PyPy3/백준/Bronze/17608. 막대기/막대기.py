import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input().rstrip()))
max_=0
count=0
for i in range(n):
    temp=arr.pop()
    if temp>max_:
        max_=temp
        count+=1    
print(count)