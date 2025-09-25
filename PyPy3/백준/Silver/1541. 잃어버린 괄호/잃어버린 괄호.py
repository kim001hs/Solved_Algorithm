import sys
def input(): return sys.stdin.readline().rstrip()
s=input()[::-1]#거꾸로 만들어서 뒤부터 계산
#-면 괄호 한 번 더나오면 괄호 풀고 -이후에 다시괄호
eax,ebx,result=0,0,0
cal=''
temp=''
if s[-1]!='-':#+부호 추가
    s+='+'
for i in s:
    if i=='-':
        eax=int(temp)
        temp=''
        if cal=='-':
            result-=ebx
            ebx=eax
        elif cal=='+':
            ebx+=eax
        else:
            ebx=eax
        cal='-'
    elif i=='+':
        eax=int(temp)
        temp=''
        if cal=='-':
            result-=ebx
            ebx=eax
        elif cal=='+':
            ebx+=eax
        else:
            ebx=eax
        cal='+'
    else:
        temp=i+temp
if cal=='+':
    result+=ebx
else:
    result-=ebx
print(result)