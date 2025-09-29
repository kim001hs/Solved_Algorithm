import sys
input = sys.stdin.readline
s=str(input().rstrip())
bomb=str(input().rstrip())

stack=[]
lenBomb=len(bomb)
for char in s:
    stack.append(char)
    if len(stack)>=lenBomb and ''.join(stack[-lenBomb:])==bomb:
        del stack[-lenBomb:]
if stack:
    print(''.join(stack))
else:
    print("FRULA")