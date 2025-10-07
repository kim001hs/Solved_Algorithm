import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
spots = [tuple(map(int, input().split())) for _ in range(n)]
count=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            d1=(spots[i][0]-spots[j][0])**2+(spots[i][1]-spots[j][1])**2
            d2=(spots[k][0]-spots[j][0])**2+(spots[k][1]-spots[j][1])**2
            d3=(spots[i][0]-spots[k][0])**2+(spots[i][1]-spots[k][1])**2
            
            if d1==d2+d3 or d2==d1+d3 or d3==d1+d2:
                count+=1
            
print(count)