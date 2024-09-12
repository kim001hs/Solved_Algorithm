a=int(input())
for i in range(a):
    b=int(input())
    clothes = {}
    for j in range(b):
        type = input().split()[1]
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    result = 1
    for i in clothes:
        result *= clothes[i] + 1
    print(result - 1)