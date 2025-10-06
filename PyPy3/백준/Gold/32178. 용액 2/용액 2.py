import sys
def input(): return sys.stdin.readline().rstrip()
INF=int(1e10)
n=int(input())
arr=list(map(int,input().split()))
min_=INF
sum_=[(0,0)]#부분합 배열
for i in range(n):
    sum_.append((sum_[-1][0]+arr[i],i+1))
sum_.sort()
for i in range(n):
    temp=sum_[i+1][0]-sum_[i][0]
    if abs(temp)<min_:
        min_=abs(temp)
        res=temp if sum_[i+1][1]>sum_[i][1] else -temp
        fir,sec=min(sum_[i][1],sum_[i+1][1])+1,max(sum_[i][1],sum_[i+1][1])
        
print(res)
print(str(fir)+' '+str(sec))