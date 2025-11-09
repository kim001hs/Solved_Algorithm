sum_=0
for i in range(5):
    temp=int(input())
    if temp<40:
        temp=40
    sum_+=temp
sum_//=5
print(sum_)