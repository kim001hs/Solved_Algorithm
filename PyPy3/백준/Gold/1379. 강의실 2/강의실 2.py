import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
heap=[]
class_=[]
res=[-1]*(n)
for i in range(n):
    no,start,end=map(int, input().split())
    heapq.heappush(heap, (start,end,no))
class_num=1
end_time,number=0,0

start,end,no=heapq.heappop(heap)
res[no-1]=class_num
heapq.heappush(class_, (end,class_num))

while heap:
    start,end,no=heapq.heappop(heap)
    end_time,class_no=heapq.heappop(class_)
    
    if start<end_time:
        class_num+=1
        heapq.heappush(class_, (end_time,class_no))
        heapq.heappush(class_, (end,class_num))
        res[no-1]=class_num
    else:
        heapq.heappush(class_, (end,class_no))
        res[no-1]=class_no
    
print(len(class_))
print(*res, sep='\n')