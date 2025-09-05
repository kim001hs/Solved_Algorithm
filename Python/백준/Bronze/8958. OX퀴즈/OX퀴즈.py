import sys
input = sys.stdin.readline  # 편하게 input()처럼 사용
n=int(input())
for i in range(n):
    ox_arr=str(input())
    result=0
    temp=0
    for j in range(len(ox_arr)):
        if(ox_arr[j]=='O'):
            temp+=1
            result+=temp
        else:
            temp=0
    print(result)
    