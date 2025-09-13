import sys
def input(): return sys.stdin.readline().rstrip()
N=input()
stack=[]
for i in N:
    if i=='[' or i =='(':
        stack.append([i,0])
    else:
        result=0
        while stack:
            prev=stack.pop()
            if (i==')' and prev[0]=='[') or (i==']' and prev[0]=='('):
                print(0)
                sys.exit()
            elif prev[0]=='[':
                if result==0:
                    stack.append(['C',3])
                else:
                    stack.append(['C',result*3])
                break
            elif prev[0]=='(':
                if result==0:
                    stack.append(['C',2])
                else:
                    stack.append(['C',result*2])
                break
            elif prev[0]=='C':
                result+=prev[1]
        else:
                print(0)
                sys.exit()
result=0
while stack:
    temp=stack.pop()
    if temp[0]!='C':
        print(0)
        sys.exit()
    result+=temp[1]
print(result)