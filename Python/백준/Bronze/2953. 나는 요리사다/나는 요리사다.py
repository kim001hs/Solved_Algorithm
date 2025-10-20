num=0
max=0
for i in range(5):
    t=sum(list(map(int,input().split())))
    if t>max:
        max=t
        num=i+1
print(str(num)+' '+str(max))