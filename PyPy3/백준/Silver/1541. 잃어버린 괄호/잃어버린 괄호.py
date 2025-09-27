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
    if i<='-':#-+일때
        ebx=int(temp)#인트로 만들어서 계산
        temp=''
        if cal=='-':
            result-=eax
            eax=ebx
        elif cal=='+':
            eax+=ebx
        else:
            eax=ebx
        if i=='-':
            cal='-'
        else:
            cal='+'
    else:
        temp=i+temp#숫자면 뒤집어놨으니까 앞에다 추가
if cal=='+':
    result+=eax
else:
    result-=eax
print(result)