a,b=map(int,input().split())
res=a*b
if res%2==0:
    print(str(res//2)+".0")
else:
    print(str(res//2)+".5")