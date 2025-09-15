import sys
def input(): return sys.stdin.readline().rstrip()
N,M,L=map(int, input().split())
shooter=list(map(int, input().split()))
shooter.sort()
animal=[]
dist=[]
L2=L**2
INF=(1e9)
for i in range(M):
    temp1,temp2=map(int,input().split())
    animal.append([temp1,temp2])
def matching(arr):
    #동물의 x값만 가져와서 사냥꾼이랑 매칭해줌
    #리턴은 x차이, y
    temp_x=arr[0]
    start=0
    end=N-1
    mid=INF
    while(start<end):
        mid=(start+end)//2
        if temp_x>shooter[mid]:
            start=mid+1
        else:
            end=mid
    if start>0 and abs(shooter[start]-temp_x)>abs(shooter[start-1]-temp_x):
        return [abs(shooter[start-1]-temp_x),arr[1]]
    return [abs(shooter[start]-temp_x),arr[1]]

def cal():
    count=0
    for i in dist:
        temp_x,temp_y=i[0],i[1]
        if temp_x+temp_y>L:
            continue
        if temp_x**2+temp_y**2>L2:
            continue
        count+=1
    return count


for i in animal:
    dist.append(matching(i))
print(cal())
    
# def cal():
    #[x차이 ,y]같은 요소들이 들어있는 배열을 받으면 계산을 해서 L보다 작은지 카운트?
    #x+y<=L이면 무조건 통과
    #x기준 정렬해서 x**2 한번 구해놓고 여러번쓰기?
    #아니면 dp표 만들어서 L이하인 크기가 L*L안 배열 미리만들고 계산?
    #O(n**2,m**2,L) 미만 목표
    #일단 L**2하려면 long long
