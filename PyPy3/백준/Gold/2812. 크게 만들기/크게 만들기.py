import sys
def input(): return sys.stdin.readline().rstrip()
N,K=map(int, input().split())
stack=[]
numbers=input()
for i in numbers:
    while stack and stack[-1]<i and K>0:
        stack.pop()
        K-=1
    stack.append(i)
while stack and K>0:
    stack.pop()
    K-=1
if not stack:
    print(0)
for i in range(len(stack)):
    print(stack[i],end='')