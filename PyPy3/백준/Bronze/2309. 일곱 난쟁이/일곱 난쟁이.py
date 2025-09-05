import sys
input = sys.stdin.readline
arr=[]
for i in range(9):
    arr.append(int(input()))
arr.sort()
sum_=sum(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if sum_-arr[i]-arr[j]==100:
            for k in range(len(arr)):
                if i!=k and j!= k:
                    print(arr[k])
            exit()