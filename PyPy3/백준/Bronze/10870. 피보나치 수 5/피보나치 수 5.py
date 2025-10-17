n=int(input())
a,b,temp=1,1,1;
for i in range(n-2):
    temp=a+b
    a,b=temp,a
if n==0:
    print(0)
else:
    print(temp)