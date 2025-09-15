import sys
def input(): return sys.stdin.readline().rstrip()
N, B=map(int, input().split())
matrix=[]

for i in range(N):
    data=list(map(int, input().split()))
    matrix.append(data)

def mul(matrix1,matrix2):#곱할 두 행렬
    C=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j]+=matrix1[i][k]*matrix2[k][j]
                C[i][j]%=1000
    return C
    
def solve(matrix, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j]%=1000
        return matrix
    
    half=solve(matrix,b//2)
    temp=mul(half, half)
    
    if b%2==1:
        return mul(temp, matrix)
    return temp
    

result=solve(matrix, B)
for i in range(N):
    for j in range(N):
        print(result[i][j], end=" ")
    print('')