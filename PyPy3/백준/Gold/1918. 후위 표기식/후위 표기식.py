import sys
def input(): return sys.stdin.readline().rstrip()
n=input()
str_stack=[]
cal_stack=[]
for char in n:
    if char>="A":
        str_stack.append(char)
        if cal_stack and (cal_stack[-1]=='*' or cal_stack[-1]=='/'):
            str_stack.append(cal_stack.pop())
        continue
    
    if char=='+' or char=='-':
        while cal_stack:
            temp=cal_stack.pop()
            if temp=='(':
                cal_stack.append(temp)
                break
            str_stack.append(temp)
            
    elif char==')':
        while cal_stack:
            temp=cal_stack.pop()
            if temp=='(':
                break
            str_stack.append(temp)
        if cal_stack and (cal_stack[-1]=='*' or cal_stack[-1]=='/'):
            str_stack.append(cal_stack.pop())
        continue
    
    cal_stack.append(char)
    
while cal_stack:
    str_stack.append(cal_stack.pop())
print(*str_stack, sep='')
