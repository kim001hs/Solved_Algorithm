import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
n=int(input())
input_=list(map(int, input().split()))
need=sum(input_)//n#한 방에 들어가야 할 수감자 수
queue=deque()
for index,i in enumerate(input_):
    if i !=need:
        queue.append([i-need,index])
del input_,need
count=0
while queue:
    temp=queue.popleft()
    if temp[0]<0:
        queue.append(temp)
    else:
        while queue:
            poped=queue.popleft()
            if poped[0]>0:
                queue.append(poped)
            else:
                count+=temp[0]*((poped[1]-temp[1])%n)
                if -poped[0]>temp[0]:
                    queue.append([poped[0]+temp[0], poped[1]])
                    break
                elif -poped[0]<temp[0]:
                    temp[0]+=poped[0]
                    temp[1]=poped[1]
                else:
                    break
print(count)