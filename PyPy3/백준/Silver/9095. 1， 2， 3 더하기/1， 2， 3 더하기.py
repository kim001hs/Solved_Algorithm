import sys
input = sys.stdin.readline
n=int(input())
arr=[1,2,4, [0]*8]
def solve(input_):
    if input_==1:
        return 1
    elif input_==2:
        return 2
    elif input_==3:
        return 4
    return solve(input_-1)+solve(input_-2)+solve(input_-3)

for i in range(n):
    input_=int(input())
    print(solve(input_))