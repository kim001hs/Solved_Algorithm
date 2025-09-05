import sys
input = sys.stdin.readline
n=int(input())
def hannoi(N, start, end, sub):
    if(N==1):
        print(str(start)+' '+str(end))
        return
    hannoi(N-1, start, sub, end)
    print(str(start)+' '+str(end))
    hannoi(N-1, sub, end, start)
    return
count = 2**n - 1
print(count)
if(n<=20):
    hannoi(n,1,3,2)
#홀짝을 판별해서 홀수면 처음을 3번으로 짝수면 2번으로
#7개면 6을 2번칸에 - 5를 3벝칸에 - 4를 2번칸에
