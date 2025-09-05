import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n= int(input())
arr=[]
bool_arr=[]
for i in range(n):
    data=list(map(int, input().split()))
    arr.append(data)

            
def removeNeighbor(i,j):
    global bool_arr
    bool_arr[i][j]=False
    if i>0:
        if bool_arr[i-1][j]:
            removeNeighbor(i-1,j)
    if j>0:
        if bool_arr[i][j-1]:
            removeNeighbor(i,j-1)
    if i<n-1:
        if bool_arr[i+1][j]:
            removeNeighbor(i+1,j)
    if j<n-1:
        if bool_arr[i][j+1]:
            removeNeighbor(i,j+1)
    return 

def solve(height):
    global bool_arr
    result=0
    bool_arr = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>height:
                bool_arr[i][j]=True
    for i in range(n):
        for j in range(n):
            if bool_arr[i][j]:
                result+=1
                removeNeighbor(i,j)
    return result

max_area=1
for i in range(0,100):
    solved=solve(i)
    if(solved>max_area):
        max_area=solved
print(max_area)
