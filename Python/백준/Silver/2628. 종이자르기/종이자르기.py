import sys
input = sys.stdin.readline
x,y=map(int, input().split())
n=int(input())
x_arr=[0,x]
y_arr=[0,y]
for i in range(n):
    a,b=map(int, input().split())
    if(a==1):
        x_arr.append(b)
    else:
        y_arr.append(b)
x_arr.sort()
y_arr.sort()
max_x=0
max_y=0
for index in range(1,len(x_arr)):
    size=x_arr[index]-x_arr[index-1]
    if(size>max_x):
        max_x=size
for index in range(1,len(y_arr)):
    size=y_arr[index]-y_arr[index-1]
    if(size>max_y):
        max_y=size
print(max_x*max_y)
