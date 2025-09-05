import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용

primeNumbers = [False, False]+[True]*(10000-1)#0과 1은 소수가 아님 나머지 10000까지는 true로 채우고 판별

#에라토스테네스의 체 n까지 검사하려면 sqrt(n까지의 인수들로 검사하면 된다)
for i in range(2,100):
    if primeNumbers[i]==True:
        for j in range(i*2, 10000, i):
            if primeNumbers[j]==True:
                primeNumbers[j] = False
            
T= int(input())

#작은 수부터 출력이고 여러가지일 경우 두 소수의 차이가 작은 것을 출력하기 때문에
#n//2 부터 검사하고 해당하는 것을 발견하면 출력 후 break한다
for i in range (T):
    n=int(input())
    for j in range (n//2, 1,-1):
        if(primeNumbers[j]==True and primeNumbers[n-j]== True):
            print(str(j)+' '+str(n-j))
            break
