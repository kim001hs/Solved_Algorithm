summ=0
minn=int(1e9)
while True:
    try:
        n=int(input())
        if n%2==1:
            summ+=n
            minn=min(minn,n)
    except EOFError:
        if summ==0:
            print(-1)
        else:
            print(summ)
            print(minn)
        break