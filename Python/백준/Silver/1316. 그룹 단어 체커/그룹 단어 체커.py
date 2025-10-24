n=int(input())
count=0
for _ in range(n):
    string=input()
    dp={}
    prevchar='A'
    for char in string:
        if prevchar==char:
            continue;
        if char in dp:
            count-=1
            break;
        prevchar=char
        dp[char]=1
    count+=1
print(count)