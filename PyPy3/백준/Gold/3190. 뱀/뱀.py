from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
n=int(input())
k=int(input())
snake=deque()
snake.append([1,1])
apple=[]
rotate=[[0,1],[1,0],[0,-1],[-1,0]]
r=0
for i in range(k):
    apple.append(list(map(int,input().split())))
L=int(input())
r=0
time=0
L_input=[]
for i in range(L):
    x,c=input().split()
    x=int(x)
    L_input.append([x,c]) 
i=0
if len(L_input)!=0:
    x,c=L_input[0][0],L_input[0][1]
while True:
    time+=1
    if time==x+1:
        i+=1
        if c=='D':
                    r=(r+1)%4
        elif c=='L':
                r=(r-1)%4
        if i<L:
            x,c=L_input[i][0],L_input[i][1]
    temp=[snake[-1][0]+rotate[r][0], snake[-1][1]+rotate[r][1]]
    if temp in snake or temp[0]==n+1 or temp[0]==0 or temp[1]==n+1 or temp[1]==0:
        print(time)
        break
    snake.append(temp)
    if temp in apple:
        apple.remove(temp)
        continue
    else:
        snake.popleft()