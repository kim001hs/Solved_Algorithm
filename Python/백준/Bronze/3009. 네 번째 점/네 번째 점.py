x,y=map(int,input().split())
a,b=x,y
x,y=map(int,input().split())
if a==x:
    a-=x
else:
    a+=x
if b==y:
    b-=y
else:
    b+=y
x,y=map(int,input().split())
if a>x:
    print(a-x,end=' ')
else:
    print(x,end=' ')
if b>y:
    print(b-y,end='')
else:
    print(y,end=' ')