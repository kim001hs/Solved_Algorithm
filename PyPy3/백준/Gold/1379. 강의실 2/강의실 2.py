import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
n=int(input())
arr=[]#입력값을 시작 시간, 끝나는 시간, 강의실 번호 순으로 저장
class_heap=[]#끝나는 시간, 깅의실 번호를 저장
res=[-1]*(n)#각 강의의 인덱스에 강의실 번호를 저장
for i in range(n):
    no,start,end=map(int, input().split())
    arr.append((start,end,no))

arr.sort()#시작시간으로 정렬

class_num=1
end_time,class_no=0,1

for start,end,no in arr:
    if class_heap:
        end_time,class_no=heapq.heappop(class_heap)
    
    if start<end_time:#강의실에 강의를 할 수 없으면
        class_num+=1#강의실 개수를 늘리고
        heapq.heappush(class_heap, (end_time,class_no))#pop한 강의실을 다시넣고
        heapq.heappush(class_heap, (end,class_num))#새로운 강의실을 추가
        res[no-1]=class_num
    else:#강의를 할 수 있으면
        heapq.heappush(class_heap, (end,class_no))#끝나는 시간만 바꿔서 넣기
        res[no-1]=class_no
    
print(class_num)
print(*res, sep='\n')