import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]
arr2=[]
for i in range(n):
    t1,t2=map(int,input().split())
    if t2<t1:#작은 수를 왼쪽으로
        t1,t2=t2,t1
    arr2.append([t1,t2])
    
d=int(input())
for i in arr2:
    if i[1]-i[0]<=d:#d보다 거리가 길면 append 안함
        arr.append(i)
arr.sort(key=lambda x:(x[1]))#end 기준 정렬
max_count=0
heap=[]#힙에서는 start기준 정렬
for i in arr:
    while heap and heap[0][0]<i[1]-d:#start가 가장 작은것부터 현재 end보다 작은 것들 pop해줌
        heapq.heappop(heap)
    
    heapq.heappush(heap, i)#현재값 넣어줌
    max_count=max(max_count,len(heap))#힙의 크기가 count
print(max_count)