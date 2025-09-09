import sys
input = sys.stdin.readline
S=str(input().rstrip())
T=str(input().rstrip())
#T를 하나씩 줄이고 비교하는 식으로 구현함(왜그랬지)
def solve(str_):
    if str_== S:#S와 같아지면 True
        return True
    if len(str_)<=len(S):#S와 다른데 길이가 같으면 False
        return False
    
    if str_[-1]=='A':#제일 뒤가 A면 없앤버전으로 재귀
        if solve(str_[:-1]):
            return True
    if str_[0]=='B':#처음이 B면 뒤집고 B없앤 버전으로 재귀
        if solve(str_[::-1][:-1]):
            return True
    return False

if solve(T):
    print(1)
else:
    print(0)