import sys
input = sys.stdin.readline
S=str(input().rstrip())
T=str(input().rstrip())

def solve(str_):
    if str_== S:
        return True
    if len(str_)<=len(S):
        return False
    
    if str_[-1]=='A':
        if solve(str_[:-1]):
            return True
    if str_[0]=='B':
        if solve(str_[::-1][:-1]):
            return True
    return False

if solve(T):
    print(1)
else:
    print(0)