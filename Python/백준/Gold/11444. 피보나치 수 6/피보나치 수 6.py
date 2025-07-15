import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
n = int(input())
MOD=1000000007

def Mul(A,B):
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            C[i][j] = 0
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= MOD
    return C

def Pibo(A, n):
    if n==1:
        return A
    temp = Pibo(A, n // 2)
    
    if(n%2 == 0):
        return Mul(temp, temp) 
    else: 
        return Mul(Mul(temp, temp), A)
    
fibo_matrix = [[1, 1], [1, 0]]
print(Pibo(fibo_matrix, n)[0][1])
    